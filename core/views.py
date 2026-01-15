from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle

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
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


class CreateSkillView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAdminPermission,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'user'


# View to list all experiences
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# Create a new experience
class CreateExperienceView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (IsAdminPermission,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'user'


# View to list all portfolio items
class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# Create a new portfolio item
class CreatePortfolioView(generics.CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAdminPermission,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'user'


# View to handle incoming messages
class MessageView(views.APIView):
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to list all messages (admin only)
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminPermission,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'user'
