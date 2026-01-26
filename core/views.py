from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle

from .models import Skill, Experience, Portfolio, Message
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


# View to list all experiences
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# Detail view for a single experience
class ExperienceDetailView(generics.RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# View to list all portfolio items
class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# Detail view for a single portfolio item
class PortfolioDetailView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'


# View to handle incoming messages (Create only via API)
class MessageCreateView(views.APIView):
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle, )
    throttle_scope = 'anon'

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
