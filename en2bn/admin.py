# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import WordList, ABValue


# Register your models here.

class WordListAdmin(admin.ModelAdmin):
    readonly_fields = ['p_hash_indx', 's_hash_indx']
    # list_filter = ['en', 'bn']
    search_fields = ['p_hash_indx', 's_hash_indx', 'en', 'bn']
    list_display = ['p_hash_indx', 's_hash_indx', 'en', 'bn']
    ordering = ['p_hash_indx']


class ABValueAdmin(admin.ModelAdmin):
    list_display = ['p_hash_indx', 'a', 'b', 'm']


admin.site.register(WordList, WordListAdmin)
admin.site.register(ABValue, ABValueAdmin)
