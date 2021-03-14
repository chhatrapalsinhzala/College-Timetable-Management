from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from classapp.models import Subject
from django.db import  transaction
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from student.serializers import StudentSerializer

from staff.models import Staff

from .forms import LoginForm
from .serializers import RegisterSerializer, StaffSerializer

User = get_user_model()
# Create your views here.
class Login(FormView):
    template_name = "web/index.html"
    title = "login"
    success_url =reverse_lazy('index')
    form_class = LoginForm
    
class Register(APIView):
    permission_classes = [AllowAny,]
    
    @transaction.atomic
    def post(self,request,format = None):
        data = self.request.data
        validated_data = user = None
        serializer = RegisterSerializer(data = data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
        try:
            user = User()
            user.first_name = validated_data.get("first_name") 
            user.last_name = validated_data.get("last_name")
            user.email = validated_data.get("email")
            user.username = validated_data.get('username')
            user.password = validated_data.get("password")
            user.save()
        except:
            raise ValidationError("Error : User alredy exist with this username")
        data = validated_data
        data["user"] = user.id
        if data["is_staff"]:
            serializer = StaffSerializer(data = data)
        else :
            serializer = StudentSerializer(data = data)
        print(data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            record = serializer.save()
            return Response(serializer.data,status=200)
        raise ValidationError("Error : Please verify the details and fill again",400)

class Logout(FormView):
    pass

# @check_permissions('teacher')
class StaffList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated, )

    # def get_queryset(self):
    #     """
    #     Return a queryset the order
    #     by the first name of user.
    #     :return:
    #     """
    #     try:
    #         queryset = super(StaffList, self).get_queryset()
    #         staff = self.request.user.staff

    #        # managers and teachers can get objects only for his locations
    #         if staff.get_role() in ['admin', 'teacher']:
    #             queryset = queryset.filter(locations__short_name__in=staff.get_locations())

    #         return queryset.order_by('user__first_name').distinct()
    #     except Exception as e:
    #         print("there is an exception")

    # @check_permissions('teacher')
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            print("this is exception") 
