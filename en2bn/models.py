# -*- coding: utf-8 -*-

from django.db import models
from .comma_separated_strings_field import CommaSeparatedStringsField, QuoteSeparatedStringsField


class WordList(models.Model):
    p_hash_indx = models.BigIntegerField()
    s_hash_indx = models.BigIntegerField()
    bn = models.CharField(max_length=100)
    en = models.CharField(max_length=100)
    bn_syns = CommaSeparatedStringsField(max_length=1000, blank=True)
    en_syns = CommaSeparatedStringsField(max_length=1000, blank=True)
    sents = QuoteSeparatedStringsField(max_length=5000, blank=True)


    def __str__(self):
        return self.en


class ABValue(models.Model):
    p_hash_indx = models.BigIntegerField()
    a = models.IntegerField()
    b = models.IntegerField()
    m = models.IntegerField(default=31)
