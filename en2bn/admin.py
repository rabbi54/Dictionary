# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import WordList, ABValue

# Register your models here.

admin.site.register(WordList)
admin.site.register(ABValue)
