from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from celery import shared_task


url = "http://localhost:9000/"
from_email = "tomas.temo77@gmail.com"
User = get_user_model()


@shared_task
def send_regestration_mail(username, email, key):
    body = f"""
    Hello {username},

    verifiy your account from link below:
    {url}account-confirm-email/{key}

    Thank You

    """
    subject = "Verify Email"
    recipients = [email]

    try:
        send_mail(
            message=body,
            subject=subject,
            from_email=from_email,
            recipient_list=recipients,
            html_message="text/html",
        )
    except Exception as exc:
        return str(exc)


@shared_task
def send_reset_password_email(user_id):
    user = User.objects.get(pk=user_id)
    body = """
    Hello %s

    reset password link below:
    %spassword/reset/confirm/%s/%s/

    Thank You

    """ % (
        user.username,
        url,
        urlsafe_base64_encode(force_bytes(user.pk)),
        default_token_generator.make_token(user),
    )

    subject = "Reset Password"
    recipients = [user.email]
    try:
        send_mail(
            message=body,
            subject=subject,
            from_email=from_email,
            recipient_list=recipients,
            html_message="text/html",
        )
    except Exception as exc:
        return str(exc)

