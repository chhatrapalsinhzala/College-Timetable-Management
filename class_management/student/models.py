from base.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Student(BaseModel):
    """
    Student model
    """
    user = models.ForeignKey(User,related_name='student_name',null=True, on_delete= models.SET_NULL)
    phone = models.CharField('Cell phone', max_length=20)
    address = models.TextField('Address', max_length=200,null=True, blank=True)
    
    def __str__(self):
        if self.student:
            return self.user.get_full_name()
        else:
            return str(self.id)

    def get_role(self):
        if self.user.is_superuser:
            return 'admin'
        elif self.user.is_staff:
            return 'teacher'
        else:
            return 'student'


class StudentInClass(BaseModel):
    """
    Student in class model shows which student is assigned to which class
    """
    comments = models.TextField(max_length=200, null=True)
    class_id = models.ForeignKey('classapp.ClassDefinition', null=True, 
                                related_name='students',
                                on_delete=models.CASCADE)
    student = models.ForeignKey(Student,
                                related_name='class_student',
                                on_delete=models.CASCADE)    
    created_by = models.ForeignKey(User, null=True,
                                   related_name='student_in_class_created_by',
                                   on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User, null=True,
                                    related_name='student_in_class_modified_by',
                                    on_delete=models.SET_NULL)
    def __str__(self):
        if self.student:
            return self.student.user.get_full_name()
        else:
            return str(self.id)