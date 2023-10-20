from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from rest_framework import routers, serializers, viewsets
from blog.models import Blog, BlogCategory


class BlogCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=BlogCategory)

    class Meta:
        model = BlogCategory
        fields = ('id', 'translations')


class BlogSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Blog)
    category = BlogCategorySerializer()
    image = serializers.ImageField()

    class Meta:
        model = Blog
        fields = ('id', 'translations', 'category', 'image', 'created', "watches")
