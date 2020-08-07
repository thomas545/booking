from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, filters, generics, views
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from allauth.account.models import EmailAddress, EmailConfirmationHMAC
from allauth.account import app_settings as allauth_settings
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.app_settings import create_token
from dj_rest_auth.views import PasswordResetView
from . import serializers, models
from .tasks import send_regestration_mail, send_reset_password_email

User = get_user_model()


class RegistrationView(RegisterView):
    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if (
            allauth_settings.EMAIL_VERIFICATION
            != allauth_settings.EmailVerificationMethod.MANDATORY
        ):
            if getattr(settings, "REST_USE_JWT", False):
                self.access_token, self.refresh_token = jwt_encode(user)
            else:
                create_token(self.token_model, user, serializer)
        email_address = EmailAddress.objects.get(user=user, email=user.email)
        confirmation_key = EmailConfirmationHMAC(email_address).key
        # TODO Send Email here -> "account-confirm-email/" + confirmation_key
        send_regestration_mail.delay(user.username, user.email, confirmation_key)
        return user


class PasswordResetView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = serializers.ResetPasswordEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, email=serializer.validated_data.get("email"))
        # TODO send email here password/reset/confirm/ + uid + "/" + token
        send_reset_password_email.delay(user.pk)
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK,
        )
