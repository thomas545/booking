from django.contrib import admin
from .models import Address, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'created',)
