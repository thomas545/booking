from django.urls import path, include
from . import views, viewsets
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="rest_register"),
    path(
        "reset/password/", views.PasswordResetView.as_view(), name="rest_password_reset"
    ),
    path("", include("dj_rest_auth.urls")),
    # path('registration/', include('dj_rest_auth.registration.urls')),
    path(
        "account-confirm-email/<str:key>/",
        VerifyEmailView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "password/reset/confirm/<str:uid>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
]
