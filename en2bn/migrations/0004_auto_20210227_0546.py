# Generated by Django 3.1.6 on 2021-02-27 05:40

import json
import random
import math
import urllib.request
from en2bn.hashing import *

from django.db import migrations

"""
This migration file resolves collision on the word list
"""


def seedData(apps, schema_editor):
    url = 'https://raw.githubusercontent.com/MinhasKamal/BengaliDictionary/master/BengaliDictionary.json'
    response = urllib.request.urlopen(url)
    ab_value = apps.get_model('en2bn', 'abvalue')
    word_list = apps.get_model('en2bn', 'wordlist')
    data = json.loads(response.read())
    for word in data:
        key = string2number(str(word['en']))
        p_hash = calculateFirstHash(key)  # done with first hash
        ab = ab_value.objects.get(p_hash_indx=p_hash)
        m = ab.m
        new_b = ab.b
        new_a = ab.a
        flag_collision = False
        first_time = False
        s_hash = calculateSecondHash(key, new_a, new_b, m)

        if word_list.objects.filter(p_hash_indx=p_hash, s_hash_indx=s_hash).count() == 1:
            first_time = True

        # collision happened
        if word_list.objects.filter(p_hash_indx=p_hash, s_hash_indx=s_hash) and not first_time:
            flag_collision = True
            m = math.sqrt(m)
            m = (m + 1) * (m + 1)
            new_a = random.randint(1, PRIME)
            new_b = random.randint(0, PRIME)
            s_hash = calculateSecondHash(key, new_a, new_b, m)

        # collision happened after changing m
        while word_list.objects.filter(p_hash_indx=p_hash,
                                       s_hash_indx=s_hash) and flag_collision and not first_time:  # while the second hash isn't unique repeat
            new_a = random.randint(1, PRIME)
            new_b = random.randint(0, PRIME)
            s_hash = calculateSecondHash(key, new_a, new_b, m)

        if flag_collision:
            updated_words = word_list.objects.filter(p_hash_indx=p_hash)
            for w in updated_words:
                update_key = string2number(w.en)
                update_s_hash = calculateSecondHash(update_key, new_a, new_b, m)
                w.s_hash_indx = update_s_hash
                w.save()

            ab = ab_value.objects.filter(p_hash_indx=p_hash)
            ab.update(a=new_a, b=new_b, m=m)
            # print(word['en'])


class Migration(migrations.Migration):
    dependencies = [
        ('en2bn', '0003_auto_20210227_0535'),
    ]

    operations = [
        migrations.RunPython(seedData)
    ]
