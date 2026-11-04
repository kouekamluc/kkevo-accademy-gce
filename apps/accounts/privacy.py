"""Personal-data export ("Download my data").

Built from the model graph rather than a hand-written list, so data added by other
apps later (anything with a CASCADE foreign key to the user) is included without
changes here. Each record also includes its own CASCADE children one level down
(e.g. a practice attempt's answers).
"""

from django.db import models

SKIPPED_APPS = {"admin", "sessions"}  # admin audit log; sessions are not personal content
USER_FIELDS = ("email", "first_name", "last_name", "date_joined", "last_login")


def _value(obj, field):
    if isinstance(field, models.ForeignKey):
        related_id = getattr(obj, field.attname)
        if related_id is None:
            return None
        return {"id": related_id, "name": str(getattr(obj, field.name))}
    return field.value_from_object(obj)


def _cascade_relations(model):
    return [
        rel for rel in model._meta.related_objects
        if rel.one_to_many and rel.on_delete is models.CASCADE
        and rel.related_model._meta.app_label not in SKIPPED_APPS
    ]


def _serialise(obj, skip_field, depth=0):
    row = {
        f.name: _value(obj, f)
        for f in obj._meta.concrete_fields
        if f.name != skip_field
    }
    if depth == 0:
        for rel in _cascade_relations(type(obj)):
            children = rel.related_model._default_manager.filter(**{rel.field.name: obj})
            row[rel.get_accessor_name()] = [_serialise(c, rel.field.name, depth + 1) for c in children]
    return row


def export_user_data(user):
    data = {"account": {name: getattr(user, name) for name in USER_FIELDS}}
    profile = getattr(user, "profile", None)
    if profile is not None:
        data["study_profile"] = _serialise(profile, "user", depth=1)
    for rel in _cascade_relations(user._meta.model):
        model = rel.related_model
        if model._meta.app_label == "accounts":
            continue  # profile handled above
        records = model._default_manager.filter(**{rel.field.name: user})
        data[rel.get_accessor_name()] = [_serialise(r, rel.field.name) for r in records]
    return data
