from .models import StudentProfile


def get_profile(user):
    """Return the user's profile, creating it for users that predate profiles."""
    try:
        return user.profile
    except StudentProfile.DoesNotExist:
        profile, _ = StudentProfile.objects.get_or_create(user=user)
        return profile
