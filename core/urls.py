from django.urls import path

from .views import (
    SkillListView,
    ExperienceListView, ExperienceDetailView,
    PortfolioListView, PortfolioDetailView,
    MessageCreateView
)


urlpatterns = [
    # Skills endpoints
    path('skills/', SkillListView.as_view(), name='skill-list'),
    
    # Experiences endpoints
    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),
    
    # Portfolio endpoints
    path('portfolios/', PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    
    # Messages endpoints (API only for creating messages)
    path('messages/send/', MessageCreateView.as_view(), name='send-message'),
]
