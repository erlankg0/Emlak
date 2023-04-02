from django.contrib import admin
from config_site.models import Favicon, Logo, Title, SubTitle


@admin.register(Favicon)
class FaviconAdmin(admin.ModelAdmin):
    pass


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    pass


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    pass


@admin.register(SubTitle)
class SubTitleAdmin(admin.ModelAdmin):
    pass
