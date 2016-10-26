from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from django.db.models import TextField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# from django.db import models

# from wagtail.wagtailcore.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)
    splash_head = TextField(blank=True)
    splash_subhead = TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        FieldPanel('splash_head', classname='full'),
        FieldPanel('splash_subhead', classname='full'),
    ]


class StaticPage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]
