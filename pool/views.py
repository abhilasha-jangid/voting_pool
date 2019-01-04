from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Pool,Option,Vote
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django import forms



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return index(request);
    else:
        form = UserCreationForm()
    return render(request, 'pool/signup.html', {'form': form})

@login_required(login_url="/login")
def index(request):
    pool = Pool.objects.filter(status = True)
    users = User.objects.all()
    context = {
        'title' : 'Choose a Pool',
        'pools' : pool,
        'user' : request.user
    } 
    return render(request,'pool/index.html',context)

def login_view(request):
    if(request.user.is_authenticated):
        return index(request)
    else:  
        return render(request,'pool/login.html')

@login_required(login_url="/login")
def details(request,id):
    vote = Vote.objects.filter(pool_id=id,user=request.user)
    if(len(vote) > 0):
        messages.info(request, 'You have already Voted!')
        return index(request)
    pool = Pool.objects.get(id=id)
    options = Option.objects.filter(pool_id=id)
    context = {
        'pool' : pool,
        'options' : options
    }
    return render(request,'pool/details.html',context)


@login_required(login_url="/login")
def submit(request,pid,oid):
    vote_obj=Vote()
    vote_obj.pool_id= Pool.objects.get(id=pid)
    vote_obj.option_id= Option.objects.get(id=oid)
    vote_obj.user=request.user
    vote_obj.save()
    return index(request)


