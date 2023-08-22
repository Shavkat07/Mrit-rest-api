from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from rest_framework import routers, serializers, viewsets
from blog.models import Blog, BlogCategory


class BlogSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Blog)

    class Meta:
        model = Blog
        fields = ('id', 'translations', 'category', 'image', 'created', "watches")
