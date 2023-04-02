from modeltranslation.translator import register, TranslationOptions
from .models import Category, Area, Rooms


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('title',)


@register(Area)
class AreaTranslationOption(TranslationOptions):
    fields = ('title',)


@register(Rooms)
class RoomsTranslationOption(TranslationOptions):
    fields = ('title',)
