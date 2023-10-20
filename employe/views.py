from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from employe.models import TeamMember, ContactPage
from employe.serializer import TeamMemberSerializer, ContactPageSerializer


class TeamMemberView(ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class ContactPageView(ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer
