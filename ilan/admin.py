from django.contrib import admin
from ilan.models import Product, Image


class ProductImages(admin.StackedInline):
    model = Image
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImages]
