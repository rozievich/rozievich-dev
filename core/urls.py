from django.urls import path

from .views import (
    SkillListView, ExperienceListView,
    PortfolioListView, MessageView
)


urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list'),
    path('messages/send/', MessageView.as_view(), name='send-message'),
]
