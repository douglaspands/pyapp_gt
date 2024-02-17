from django.core.management.base import BaseCommand, CommandError

from communication.services import email


class Command(BaseCommand):
    help = "Check Send Email"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sender: str = "Sender Check <sender@check.com>"
        to: list[str] = ["Receive Check <receive@check.com>"]
        subject: str = "Subtitle Check"
        message: str = "# Title Check\n\nMessage content check."

        email.send_email(sender=sender, to=to, subject=subject, message=message)
        self.stdout.write(self.style.SUCCESS("Send Email Checked"))
