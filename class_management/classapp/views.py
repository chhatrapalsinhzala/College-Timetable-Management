from rest_framework import serializers
from base.methods import convert_to_date
from datetime import datetime,timedelta
import calendar

from classapp.models import ClassDefinition
from django.http import response
from classapp.models import Subject
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import  transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from django.conf import settings
from base.decorators import check_permissions
from .serializers import SubjectSerializer,ClassDefinitionSerializer

# Create your views here.

class SubjectView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data,200)

    @transaction.atomic
    def post(self, request):
        data = request.data
        serializer = SubjectSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,200)
        raise("Error : Did not able to create Subject",400)

    @transaction.atomic
    def put(self, request):
        data = request.data
        subject = None
        try :
            subject = Subject.objects.get(id = data.get("id"))
        except:
            raise ValidationError("There are no subject available for this Id")

        serializer = SubjectSerializer(instance = subject , data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,200)
        raise("Error : Did not able to update subject details",400)


class CreateClassView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        classes = ClassDefinition.objects.filter(is_deleted = False).order_by("class_date","start_time")
        serializer = ClassDefinitionSerializer(classes, many = True)

        return Response(serializer.data,200)

    @transaction.atomic
    @check_permissions('TEACHER')
    def post(self , request):
        data = request.data
        data['created_by'] = request.user.id
        data['modified_by'] = request.user.id
        serializer = ClassDefinitionSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data


            class_date = validated_data.get("class_date")
            staff = validated_data.get("staff")
            
            #check if its not saturday or sunday 
            weekday = calendar.day_name[class_date.weekday()].lower()
            if weekday == "sunday" or weekday == "saturday" :
                return Response("Error: You can not schedule classes on saturday or sunday.",400)
            today = datetime.today()
            last_monday = today - timedelta(days= -today.weekday(),weeks=1)
            next_friday = last_monday + timedelta(4)
            #logic to find if there are more then 25 classes in a week which are between monday and friday
            classes = ClassDefinition.objects.filter(class_date__gte = last_monday,class_date__lte = next_friday)
            if len(classes) > 25:
                return Response("Error: You can not create more then 25 classes in a week.",400)
            
            # Teacher can not create classes more then 18 hours a week.
            classes = classes.filter(staff = staff)
            if len(classes) > 18 :
                return Response("Error: Teacher can not have more then 18 classes in a week.",400)

            #logic to check if staff have more then 4 classes in a single day
            classes = classes.filter(class_date = class_date)
            if len(classes) > 4:
                return Response("Error: Teacher can not have more then 4 classes on single day.",400)

            #logic to find classes which are scheduled on the input class date
            classes = ClassDefinition.objects.filter(class_date = class_date)
            if len(classes) > 6:
                return Response("Error: You can not create more then 6 classes on single day.",400)
            else : 
                serializer.save()
        return Response(serializer.data,200)

    @transaction.atomic
    @check_permissions('TEACHER')
    def delete(self , request):
        data = request.data
        data['created_by'] = request.user.id
        data['modified_by'] = request.user.id
        class_instance = None
        try :
            class_instance = ClassDefinition.objects.get(id = data.get("id"))
        except Exception as e:
            return Response("There are no class available for this Id" , 400)

        serializer = ClassDefinitionSerializer(instance = class_instance , data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,200)
        return Response("Error : could not cancelled the class",400)
        