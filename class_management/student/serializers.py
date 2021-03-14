from rest_framework.exceptions import ValidationError
from classapp.models import ClassDefinition
from rest_framework import serializers
from .models import Student, StudentInClass

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentInClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInClass
        fields = "__all__"
    
    def validate(self, data):
        student = data.get("student")
        class_id = data.get("class")
        print(student,class_id)
        if student and  student.is_deleted == True:
            raise serializers.ValidationError("Student do not exist any more.")
        class_def = ClassDefinition.objects.filter(id = class_id, is_deleted = True)
        if class_def.exists():
            raise serializers.ValidationError("class does not exist any more.")
        return data