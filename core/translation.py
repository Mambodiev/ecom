from modeltranslation.translator import (
    translator,
    register,
    TranslationOptions,
)
from core.models import About,Faq,Privacy_policy,Shipping_returns,Terms_of_use


class AboutTranslationsOptions(TranslationOptions):
    fields = ('about_text',)


class FaqTranslationsOptions(TranslationOptions):
    fields = ('faq_text',)


class Privacy_policyTranslationsOptions(TranslationOptions):
    fields = ('privacy_policy_text',)


class Shipping_returnsTranslationsOptions(TranslationOptions):
    fields = ('shipping_returns_text',)


class Terms_of_useTranslationsOptions(TranslationOptions):
    fields = ('terms_of_use_text',)




translator.register(About, AboutTranslationsOptions)
translator.register(Faq, FaqTranslationsOptions)
translator.register(Privacy_policy, Privacy_policyTranslationsOptions)
translator.register(Shipping_returns, Shipping_returnsTranslationsOptions)
translator.register(Terms_of_use, Terms_of_useTranslationsOptions)