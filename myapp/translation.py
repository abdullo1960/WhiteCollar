from modeltranslation.translator import register, TranslationOptions
from .models import Info, Contact, BlogModel, MessageModel


@register(Contact)
class  ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'text')



@register(BlogModel)
class  BlogModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'tarif')


@register(MessageModel)
class  MessageModelTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'subject', 'text')