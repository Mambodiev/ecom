from modeltranslation.translator import (
    translator,
    register,
    TranslationOptions,
)
from cart.models import Product, ColourVariation, SizeVariation


class ColourVariationTranslationsOptions(TranslationOptions):
    fields = ('name',)


class SizeVariationTranslationsOptions(TranslationOptions):
    fields = ('name',)


class ProductTranslationsOptions(TranslationOptions):
    fields = ('title', 'slug', 'primary_category')
    empty_values = {'slug': None}



translator.register(ColourVariation, ColourVariationTranslationsOptions)
translator.register(SizeVariation, SizeVariationTranslationsOptions)
translator.register(Product, ProductTranslationsOptions)