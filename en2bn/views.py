# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView
from .hashing import *
from .models import WordList, ABValue
from rest_framework.decorators import api_view
from .serializers import WordSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def search(request):
    word = request.GET['word'].strip().casefold()
    key = string2number(word)
    p_hash = calculateFirstHash(key)
    abm = ABValue.objects.get(p_hash_indx=p_hash)
    a = abm.a
    b = abm.b
    m = abm.m

    s_hash = calculateSecondHash(key, a, b, m)
    w = WordList.objects.get(p_hash_indx=p_hash, s_hash_indx=s_hash)
    print(w)
    if w.en == word:
        serializer = WordSerializer(w)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class IndexView(TemplateView):
    template_name = 'index.html'
