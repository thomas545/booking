from rest_framework import serializers


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
