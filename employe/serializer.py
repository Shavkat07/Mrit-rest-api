from employe.models import TeamMember
from rest_framework import serializers


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id', 'name', 'role', 'about', 'image', 'telegram',
                  'instagram', 'linkedin',)
