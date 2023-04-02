from modeltranslation.translator import register, TranslationOptions

from ilan.models import Product


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ('title', 'description',)

