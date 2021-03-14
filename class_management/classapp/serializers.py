from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers
from staff.models import Staff
from .models import Subject,ClassDefinition

from django.contrib.auth import get_user_model
User = get_user_model()

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ClassDefinitionSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    class_date = serializers.DateField(required=True)
    duration = serializers.CharField(required=True)
    class_status = serializers.CharField(required=True)

    class Meta:
        model= ClassDefinition
        fields = "__all__"
    



