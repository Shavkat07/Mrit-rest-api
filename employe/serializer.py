from employe.models import TeamMember, ContactPage
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField


class TeamMemberSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=TeamMember)

    class Meta:
        model = TeamMember
        fields = ('id', 'role', 'image', 'telegram',
                  'instagram', 'linkedin', 'github', 'translations')


class ContactPageSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ContactPage, read_only=True)

    class Meta:
        model = ContactPage
        fields = ('id', 'full_name', 'username', 'email', 'telegram', 'translations')
