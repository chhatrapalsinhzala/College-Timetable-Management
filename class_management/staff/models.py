from django.db import models
from django.contrib.auth import get_user_model
from classapp.models import BaseModel
User = get_user_model()


class Tpken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField()



class StaffModelManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(active = True)

# Create your models here.
class Staff(BaseModel):
    """
    Staff model to store all staff info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=20)
    address = models.TextField('Address', max_length=200,null=True, blank=True)
    joining_date = models.DateField('joining date', null=True)
    active = models.BooleanField(default=True)
    

    objects = StaffModelManager()

    def __str__(self):
        return self.user.get_full_name()

    def get_role(self):
        if self.user.is_superuser:
            return 'admin'
        elif self.user.is_staff:
            return 'teacher'
        else:
            return 'student'

    