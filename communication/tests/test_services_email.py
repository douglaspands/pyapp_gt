from django.test import TestCase

from communication.services import email


class EmailServiceTestCase(TestCase):

    def test_send_email(self):
        """Send email"""

        # EXPECT
        res_expect = 1
        subject_expect = "Subject here"

        # GIVEN
        sender: str = "from@example.com"
        to: list[str] = ["to@example.com"]
        subject: str = subject_expect
        message: str = "Here is the message."

        # WHEN
        res = email.send_email(sender=sender, to=to, subject=subject, message=message)

        # THEN
        self.assertEqual(res, res_expect)
        self.assertEqual(email._django_mail.outbox[0].subject, subject_expect)
