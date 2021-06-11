from django.forms import ModelForm
from .models import Interview
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ['title', 'date', 'start_time', 'end_time']
        widgets = {
            'date': DateInput(),
            'start_time' : DateTimeInput(),
            'end_time' : DateTimeInput()
        }

