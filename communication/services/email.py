from django.core import mail as _django_mail


def send_email(sender: str, to: list[str], subject: str, message: str) -> int:
    result = _django_mail.send_mail(
        subject,
        message,
        sender,
        to,
        fail_silently=False,
    )
    # with __django_mail.get_connection() as connection:
    #     result = __django_mail.EmailMessage(
    #         subject=subject,
    #         body=message,
    #         from_email=sender,
    #         to=to,
    #         connection=connection,
    #     ).send()

    return result


__all__ = ("send_email",)
