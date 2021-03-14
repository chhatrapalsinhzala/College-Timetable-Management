from datetime import datetime,timedelta
from django.db.models import Q
import traceback
from classapp.models import ClassDefinition
from django.db import  transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from base.decorators import check_permissions
from.models import StudentInClass
from .serializers import StudentInClassSerializer

# Add student in class.

class AddStudentInClass(APIView):
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        today = datetime.today().date()
        classes = StudentInClass.objects.filter(class_id__class_date__gte = today,is_deleted = False).order_by("class_id__class_date","class_id__start_time")
        serializer = StudentInClassSerializer(classes, many = True)

        return Response(serializer.data,200)

    @transaction.atomic
    @check_permissions('TEACHER')
    def post(self , request):
        data = request.data
        data['created_by'] = request.user.id
        data['modified_by'] = request.user.id
        serializer = StudentInClassSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data

            student_id = validated_data.get("student")
            class_id = validated_data.get("class_id")
            class_def = None
            try:
                class_def = ClassDefinition.objects.filter(id = class_id.id , class_status ="scheduled" ).last()
            except Exception as e:
                print(traceback.format_exc())
                return Response ("There are no class on this class id",400)
            class_date = class_def.class_date
            start_time = class_def.start_time
            end_time = class_def.end_time

            today = datetime.today()
            last_monday = today - timedelta(days= -today.weekday(),weeks=1)
            next_friday = last_monday + timedelta(4)
            #logic to find if there are more then 25 classes in a week which are between monday and friday
            classes = StudentInClass.objects.filter(student = student_id,class_id__class_date__gte = last_monday,is_deleted = False, class_id__class_date__lte = next_friday)
            if len(classes) > 25:
                return Response("Error: Student can not enroll more then 25 classes in a week.",400)

            #logic to find classes which are scheduled on the input class date
            classes = StudentInClass.objects.filter(class_id__class_date = class_date, is_deleted = False)
            if len(classes) > 6:
                return Response("Error: Student can not enroll more then 6 class in a single day.",400)
            overlapping_classes = StudentInClass.objects.filter(class_id__class_date = class_date,student = student_id, is_deleted = False) \
                                                        .filter(Q(class_id__start_time__lte=start_time, class_id__end_time__gt=start_time) |
                                                        Q(class_id__start_time__gt=end_time, class_id__end_time__lte=end_time))
            if overlapping_classes:
                return Response("Error: Student is alredy enrolled in other class in this time period.")
            else : 
                serializer.save()
        return Response(serializer.data,200)

    @transaction.atomic
    @check_permissions('TEACHER')
    def delete(self , request):
        data = request.data
        data['modified_by'] = request.user.id
        class_instance = None
        try :
            class_instance = StudentInClass.objects.get(id = data.get("id"),is_deleted = False)
        except Exception as e:
            return Response("Student is not assigned to this class" , 400)

        serializer = StudentInClassSerializer(instance = class_instance , data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,200)
        return Response("Error : could not remove student from the class the class",400)
