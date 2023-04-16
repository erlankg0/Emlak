from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from ilan.models import Product, Image, Favorite, RoomsImage


class ProductImages(admin.StackedInline):
    model = Image
    extra = 2


class RoomsImages(admin.StackedInline):
    model = RoomsImage
    extra = 2


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImages, RoomsImages]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
