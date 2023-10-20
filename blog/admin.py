from django.contrib import admin

from blog.models import Blog, BlogCategory
from parler.admin import TranslatableAdmin


class BlogCategoryAdmin(TranslatableAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BlogAdmin(TranslatableAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title', 'text')
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'category', "image"),
        }),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
