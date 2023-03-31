from modeltranslation.translator import register, TranslationOptions
from config_site.models import Title, SubTitle


@register(Title)
class TitleTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SubTitle)
class SubTitleTranslationOptions(TranslationOptions):
    fields = ('name',)
