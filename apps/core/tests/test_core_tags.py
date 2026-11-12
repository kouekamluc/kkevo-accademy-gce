from datetime import timedelta

from django.utils import timezone

from apps.core.templatetags.core_tags import ago


def test_ago_says_just_now_under_a_minute():
    assert ago(timezone.now() - timedelta(seconds=20)) == "just now"
    assert ago(None) == ""


def test_ago_uses_the_biggest_unit_only():
    assert ago(timezone.now() - timedelta(minutes=5, seconds=3)) == "5 minutes ago"
    assert ago(timezone.now() - timedelta(hours=2, minutes=10)) == "2 hours ago"
    assert ago(timezone.now() - timedelta(days=3, hours=4)) == "3 days ago"
