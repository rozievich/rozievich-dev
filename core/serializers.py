from rest_framework import serializers

from .models import Skill, Experience, Portfolio, Message


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    

class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id', 'company_name', 'company_url', 'position',
            'skills', 'start_date', 'end_date', 'description',
            'is_current', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class PortfolioSerializer(serializers.ModelSerializer):
    tech_skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'id', 'title', 'image', 'description',
            'project_url', 'tech_skills', 'is_future', 'github_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id', 'name', 'email', 'subject',
            'body', 'is_read', 'sent_at'
        ]
        read_only_fields = ['is_read', 'sent_at']
