import imp
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from InternManager.models import Task
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request, 'main.html')
def TaskItem(request):
    all_tasks = Task.objects.all()
    context = {
        'all_tasks': all_tasks
    }
    return render(request, 'base.html', context)

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_Intern:
                login(request, user)
                return redirect('Intern')
            elif user is not None and user.is_SuperVisor:
                login(request, user)
                return redirect('superVisor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def intern(request):
    return render(request, 'Intern.html')

def superVisor(request):
    return render(request, 'SuperVisor.html')