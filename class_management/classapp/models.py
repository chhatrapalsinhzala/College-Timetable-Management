from django.db import models
from django.contrib.auth import get_user_model
from base.models import BaseModel

User = get_user_model()



# Create your models here.
class Subject(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ClassDefinition(BaseModel):
    """
    class definition model to store all class details
    """
    STATUSES_CHOICES = (('scheduled', 'Scheduled'), 
                        ('cancelled', 'Cancelled'))

    start_time = models.TimeField('Start time',null = True, blank = True)
    end_time = models.TimeField('End time',null = True, blank = True)
    class_date = models.DateTimeField('Class date', null = True, blank = True)
    weekday = models.CharField('Weekday', max_length=20, null=True)
    staff = models.ForeignKey("staff.Staff", verbose_name='Teacher', related_name='teacher',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name='subject', related_name='subject',on_delete=models.CASCADE)
    duration = models.CharField("Class Duration",max_length=255)
    class_status = models.CharField('Class status', max_length=200, choices=STATUSES_CHOICES, default='scheduled')
    created_by = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='class_definition_creator')
    modified_by = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='class_definition_modifier')
    
    def __str__(self):
        if self.student:
            return self.student.user.get_full_name()
        else:
            return str(self.id)



