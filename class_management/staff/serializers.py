from rest_framework import serializers
from staff.models import Staff
from student.models import Student
from django.contrib.auth import get_user_model
User = get_user_model()

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True , min_length = 8 , style = {"input_type" : "password"})
    confirm_password = serializers.CharField(required=True, min_length = 8,style = {"input_type" : "password"})
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_staff = serializers.BooleanField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    joining_date = serializers.DateField(required=False)

    def validate(self, data):
        phone = data.get("phone", None)
        email = data.get("email", None)
        password = data.get("password", None)
        confirm_password = data.get("confirm_password", None)
        user = User.objects.filter(email = email)
        if user.exists():
            raise serializers.ValidationError("User alredy exist with this email Id")
        student = Student.objects.filter(phone = phone)
        if student.exists():
            raise serializers.ValidationError("User alredy exist with this phone no.")
        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm Password are not same")
        return data
    




