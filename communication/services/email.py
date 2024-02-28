from django.core import mail as _django_mail

from communication.resources.email import Email


def send_email(email: Email) -> int:
    result = _django_mail.send_mail(
        subject=email.subject,
        message=email.message,
        from_email=email.sender,
        recipient_list=email.to,
        fail_silently=False,
    )
    return result


__all__ = ("send_email",)
