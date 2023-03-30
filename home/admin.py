from django.contrib import admin
from home.models import Category, Area, Rooms, Ip


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    pass


@admin.register(Ip)
class IPAdmin(admin.ModelAdmin):
    pass
