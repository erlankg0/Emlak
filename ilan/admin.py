from django.contrib import admin
from ilan.models import Product, Image
from modeltranslation.admin import TranslationAdmin


class ProductImages(admin.StackedInline):
    model = Image
    extra = 2


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImages]
