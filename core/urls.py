from django.urls import path

from .views import (
    SkillListView, CreateSkillView
)

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('skills/create/', CreateSkillView.as_view(), name='create-skill'),
]
