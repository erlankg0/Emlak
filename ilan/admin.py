from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from ilan.models import Product, Image


class ProductImages(admin.StackedInline):
    model = Image
    extra = 2


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImages]
    prepopulated_fields = {"slug": ("title",)}
