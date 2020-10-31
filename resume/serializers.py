from rest_framework import serializers
from .models import Project, Resume


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'sub_discription', 'discription', 'language', 'summary',
                'created_at', 'slug', 'github', 'website']

class ResumeSerializers(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Resume
        fields = ['id', 'name', 'experience', 'image', 'github', 'linkedin', 'degree', 'college',
         'university', 'email', 'website', 'projects']

