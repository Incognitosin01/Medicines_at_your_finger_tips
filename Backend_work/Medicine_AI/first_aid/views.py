from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required(login_url='home')
def acc_emerg(request):
    return render(request,"HTML/accidents_n_emergencies.html")

@login_required(login_url='home')
def gloss(request):
    return render(request,"HTML/first_aid_gloss.html")

@login_required(login_url='home')
def info(request):
    return render(request,"HTML/first_aid_info.html")

@login_required(login_url='home')
def kit(request):
    return render(request,"HTML/first_aid_kit.html")