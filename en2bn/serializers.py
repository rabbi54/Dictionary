from rest_framework import serializers
from .models import WordList


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordList
        fields = '__all__'
