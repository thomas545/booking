from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tomas.temo77@gmail.com'
EMAIL_HOST_PASSWORD = '23103280'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Celery Settings
CELERY_BROKER_URL = 'amqp://localhost'


# GRAPPELLI Settings
GRAPPELLI_ADMIN_TITLE = "Booking"