from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework.permissions import AllowAny

from .models import Skill, Experience, Portfolio, Message
from .permissions import IsAdminPermission
from .serializers import (
    SkillSerializer, ExperienceSerializer,
    PortfolioSerializer, MessageSerializer
)


# View to list all skills
class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)


class CreateSkillView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAdminPermission,)


# View to list all experiences