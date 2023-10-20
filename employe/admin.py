from django.contrib import admin

from employe.models import TeamMember, ContactPage
from parler.admin import TranslatableAdmin


class TeamMemberAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'role')
    list_display_links = ('id', 'name', 'role')
    fieldsets = (
        (None, {
            'fields': ('name', 'about', 'role', "image",
                       "telegram", 'instagram', 'linkedin', 'github'),
        }),
    )


admin.site.register(TeamMember, TeamMemberAdmin)


class ContactPageAdmin(TranslatableAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')


admin.site.register(ContactPage, ContactPageAdmin)
