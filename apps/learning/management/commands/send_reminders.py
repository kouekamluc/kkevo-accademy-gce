from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.accounts.models import StudentProfile
from apps.learning import reminders


class Command(BaseCommand):
    help = "Send today's study reminders to students whose chosen hour has come. Run it every hour."

    def add_arguments(self, parser):
        parser.add_argument("--dry-run", action="store_true", help="List who would get an email without sending.")

    def handle(self, *args, dry_run=False, **options):
        now = timezone.localtime()
        today = now.date()
        due = (StudentProfile.objects.filter(reminders_enabled=True, user__is_active=True, reminder_hour__lte=now.hour)
               .exclude(last_reminder_on=today).exclude(user__email="").select_related("user"))
        sent = 0
        for profile in due:
            if dry_run:
                if reminders.build(profile.user, today):
                    self.stdout.write(f"would send to {profile.user.email}")
                continue
            try:
                ok = reminders.send_for(profile.user, today)
            except Exception as exc:  # one bad address must not stop everyone else
                self.stderr.write(f"{profile.user.email}: {exc}")
                continue
            # Mark the day as handled even when there was nothing to say, so we do not recompute every hour.
            StudentProfile.objects.filter(pk=profile.pk).update(last_reminder_on=today)
            sent += ok
        self.stdout.write(f"{sent} reminder(s) sent")
