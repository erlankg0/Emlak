from django.contrib import admin
from home.models import Category, Area, Rooms, Ip
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    model = Category
    translation_fields = ('title',)


@admin.register(Area)
class AreaAdmin(TranslationAdmin):
    pass


@admin.register(Rooms)
class RoomsAdmin(TranslationAdmin):
    pass


@admin.register(Ip)
class IPAdmin(admin.ModelAdmin):
    pass
