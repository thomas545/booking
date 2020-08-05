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

User = get_user_model()

class RegistrationView(RegisterView):
    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if allauth_settings.EMAIL_VERIFICATION != \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            if getattr(settings, 'REST_USE_JWT', False):
                self.access_token, self.refresh_token = jwt_encode(user)
            else:
                create_token(self.token_model, user, serializer)
        email_address = EmailAddress.objects.get(user=user, email=user.email)
        confirmation_key = EmailConfirmationHMAC(email_address).key
        # TODO Send Email here -> "account-confirm-email/" + confirmation_key
        
        return user

class PasswordResetView(views.APIView):
    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email_address = request.data.get("email", None)
        user = get_object_or_404(User, email=email_address)

        from django.utils.encoding import force_bytes
        from django.contrib.auth.tokens import default_token_generator
        from django.utils.http import urlsafe_base64_encode

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        # TODO send email here users/password/reset/confirm/" + uid + "/" + token

        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK
        )