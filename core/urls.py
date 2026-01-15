from django.urls import path

from .views import (
    SkillListView, CreateSkillView,
    ExperienceListView, CreateExperienceView,
    PortfolioListView, CreatePortfolioView,
    MessageListView, MessageView
)


urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('skills/create/', CreateSkillView.as_view(), name='create-skill'),
    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('experiences/create/', CreateExperienceView.as_view(), name='create-experience'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolios/create/', CreatePortfolioView.as_view(), name='create-portfolio'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/send/', MessageView.as_view(), name='send-message'),
]
