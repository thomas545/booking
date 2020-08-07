from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Realty, Room, RealtyImage, RoomImage

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass

@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(RealtyImage)
class RealtyImageAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass

