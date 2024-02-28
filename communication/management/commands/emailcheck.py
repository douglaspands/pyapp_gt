from django.core.management.base import BaseCommand, CommandError

from communication.resources.email import Email
from communication.services import email as email_service


class Command(BaseCommand):
    help = "Check Send Email"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        e = Email(
            sender="Sender Check <sender@check.com>",
            to=["Receive Check <receive@check.com>"],
            subject="Subtitle Check",
            message="# Title Check\n\nMessage content check.",
        )
        email_service.send_email(e)
        self.stdout.write(self.style.SUCCESS("Send Email Checked"))
