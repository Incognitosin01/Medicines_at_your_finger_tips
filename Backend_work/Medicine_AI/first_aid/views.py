from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

def acc_emerg(request):
    return render(request,"HTML/accidents_n_emergencies.html")

def gloss(request):
    return render(request,"HTML/first_aid_gloss.html")

def info(request):
    return render(request,"HTML/first_aid_info.html")

def kit(request):
    return render(request,"HTML/first_aid_kit.html")