from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length = 40)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    college = models.CharField(max_length = 100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    position_applied = models.CharField(max_length = 30, blank = True, null = True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

