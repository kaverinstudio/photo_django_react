from modeltranslation.translator import register, TranslationOptions
from .models import MainCardModel

@register(MainCardModel)
class MainCardTranslation(TranslationOptions):
    fields = ['description',]