from dataclasses import fields
from rest_framework import serializers

from .models import News

# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     desc = serializers.CharField()
#     author = serializers.CharField()
#     create_date = serializers.DateTimeField()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = ['id', 'title', 'desc', 'author', 'create_date']
        fields = '__all__'


