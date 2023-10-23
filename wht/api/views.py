from rest_framework import viewsets
from .models import Team, Member
from .serializers import TeamSerializer, MemberSerializer
from .permissions import IsOwnerOrReadOnly


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
