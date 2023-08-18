from rest_framework import serializers

from blog.models import Blog, BlogCategory


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name')


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()

    class Meta:
        model = Blog
        fields = ("id", 'category', 'title', 'image', 'text', 'created', 'watches')
