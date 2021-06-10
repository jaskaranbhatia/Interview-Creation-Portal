from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Interview, InterviewParticipants
from .forms import InterviewForm

# Create your views here.
def home(request):
    return render(request, 'interviews/home.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'interviews/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'interviews/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('get_interviews')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def get_interviews(request):
    interviews = Interview.objects.all()
    return render(request , 'interviews/listings.html', { 'interviews':interviews } )


@login_required
def create_interview(request):
    if request.method == 'GET':
        return render(request, 'interviews/createInterview.html', {'form':InterviewForm})
    else:
        try:
            form = InterviewForm(request.POST)
            newInterview = form.save(commit=False)
            newInterview.save()
            newInterviewParticipants = InterviewParticipants(interview = newInterview)
            newInterviewParticipants.save()
            return redirect('get_interviews')
        except ValueError:
            return render(request, 'interviews/createInterview.html', {'form':InterviewForm(), 'error':'Bad Data Passed'})
