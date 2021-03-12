from django.db import models
from django.contrib.auth import get_user_model
from classapp.models import BaseModel
User = get_user_model()


# Create your models here.
class Staff(BaseModel):
    """
    Staff model to store all staff info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell_phone = models.CharField('Phone', max_length=20)
    street = models.CharField('Street', null=True, max_length=200)
    city = models.CharField('City', null=True, max_length=200)
    zip = models.CharField('Zip code', null=True, max_length=20)
    joining_date = models.DateField('joining date', null=True)
    date_of_birth = models.DateField('Date of birth', null=True)
    photo = models.TextField('Photo', null=True, blank=True)
    subjects = models.ManyToManyField('classapp.Subject', related_name='staff_subjects')

    def __str__(self):
        return self.user.get_full_name()



