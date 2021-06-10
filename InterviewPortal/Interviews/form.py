from django.forms import ModelForm
from .models import Interview

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ['title', 'date', 'start_time', 'end_time']