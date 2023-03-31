from modeltranslation.translator import register, TranslationOptions
from ilan.models import Product, Category, Area, Rooms


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'category', 'square', 'rooms', 'area')


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('title',)


@register(Area)
class AreaTranslationOption(TranslationOptions):
    fields = ('title',)


@register(Rooms)
class RoomsTranslationOption(TranslationOptions):
    fields = ('title',)
