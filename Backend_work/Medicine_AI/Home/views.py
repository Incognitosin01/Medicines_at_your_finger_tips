import sys,os
from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact_us,medicine,side_effect
from my_med_list.models import Med_list
from django.contrib import messages
import json
from django.http import JsonResponse
from .chatbot import getresponse
import re
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import random

#from Data.drugs_list import Drugs_List

# Create your views here.
Random_token=str(random.randint(100000,999999))

def check_password(password_1):
    c=0
    if len(password_1)>7:
        c+=1
    if not password_1.isalpha():
        c+=1
    if  not password_1.isnumeric():
        c+=1
    if not password_1.isalnum():
        c+=1
    if c==4:
        return True
    else:
        return False

def check_mail(mail):
    # print(mail)
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    # print(regex)
    if (re.search(regex,mail)):
        return True
    else:
        return False

def Home(request):
    
    return render(request,'HTML/index.html')

@login_required(login_url='home')
def about(request):
    return render(request,'HTML/about.html')

@login_required(login_url='home')
def side_effects(request):

    return render(request,'HTML/side_effects.html')

@login_required(login_url='home')
def contact_us(request):
    return render(request,'HTML/contact_us.html')

@login_required(login_url='home')
def drug_A_Z(request):
    return render(request,'HTML/Drugs_a-z.html')

@login_required(login_url='home')
def drug_cond(request):
    return render(request,'HTML/drugs_by_condition.html')

@login_required(login_url='home')
def first_aid(request):
    return render(request,'HTML/first_aid.html')

@login_required(login_url='home')
def symptom_checker(request):
    return render(request,'HTML/Symptom_checker.html')

@login_required(login_url='home')
def med_list(request):
    all_medications = Med_list.objects.all()
    return render(request,'HTML/My_med_list.html',{"val":all_medications})

def sign_up(request):
    #print("hello") 
    if request.method == 'POST':
        global Username
        Username=request.POST['Username']
        global First_name
        First_name=request.POST['First_name']
        global Last_name
        Last_name=request.POST['Last_name']
        global Email 
        Email= request.POST['Email']
        global password_1
        password_1 = request.POST['Password1']
        global password_2 
        password_2= request.POST['Password2']

        if password_1==password_2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username Taken ,Please provide some unique Username')
                return redirect('home')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,'Email ID already exists!')
                return redirect('home')
            else:
                
                x=check_password(password_1)
                y=check_mail(Email)
                if x==False:
                     messages.error(request,' Password Given is not strong enough . Please provide Password which has minimum length 8 characters with numbers and special characters')
                     return redirect('home')
                if y==False:
                    messages.error(request,"Email Provided is Invalid. Please provide valid Email ID")
                    return redirect('home')

                else:
                    
                    html_message = loader.render_to_string(
                                'HTML/mail_body.html',
                                {
                                    'user_name' : Username,
                                    'first_name'  :First_name,
                                    'last_name' : Last_name,
                                    'token' : Random_token,
                                }
                            )
                    send_mail('CONFIRMATION',None,settings.EMAIL_HOST_USER,[Email],fail_silently=True,html_message=html_message)
                    
                    return render(request,'HTML/confirm_template.html')
                    # ch = check_token(request)
                    # if ch==True:
                    #     user = get_user_model().objects.create_user(username=Username,email=Email,password=password_1,first_name=First_name,last_name=Last_name)
                    #     messages.success(request,"Successfully Sign In!")
                    #     return redirect('home')
                    # else:
                    #     messages.error(request,'Token entered was incorredct. Please Sign In again')
                    #     return redirect('home')
                    
                    # send_mail(
                    #     'CONFIRMATION',
                    #     'HELLO LAADDU!!\nMAZA LAADU TU MERI JAAN HE',
                    #     settings.EMAIL_HOST_USER,
                    #     [Email],
                    #     fail_silently=False,
                    # )
                    # user.save()
                    # return render(request,'HTML/mail_body.html')
                    
        else:
            messages.error(request,' Both Password enetered not matching')
            return redirect('home')
    else:
        return HttpResponse("<h1>Error 404</h1>")   

def handle_login(request):

    if request.method == 'POST':
        Username = request.POST.get('Username')
        password_1 = request.POST.get('Password1')
        user = auth.authenticate(username = Username,password=password_1)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
            
        else:
            messages.error(request,"Invalid Credentials , Please try again!")
            return redirect('home')
    else:
        return HttpResponse("<h1>Error 404</h1>")

def handle_logout(request):
    if request.method == "GET":
        logout(request)
        messages.success(request,"Successfully Logged Out!")
        return redirect('home')
    else:
        return HttpResponse("<h1>Error 404</h1>")

def search(request) : 
    if request.method == 'GET':
        if 'term' in request.GET:
            qs = medicine.objects.filter(name__istartswith = request.GET['term'])
            vs = side_effect.objects.filter(name__istartswith = request.GET['term'])
            names = []
            counter=10
            for i in qs:
                names.append(i.name)
                counter-=1
                if counter==5:
                    break
            for i in vs:
                names.append(i.name)
                counter-=1
                if counter==0:
                    break
            return JsonResponse(names,safe=False)
        x = request.GET['query']
        z = x.replace(' ','')
        if('-side-effect' in x):

            z = x.replace('-side-effect','')
            med_list = list(side_effect.objects.values_list('name', flat=True))
            if x in med_list:
                return render(request,'Data\\side_effects2\\'+z+".html")
            else:
                messages.warning(request,"Medicine provided is invalid or may not be available in DB")
                return redirect('home')
        else:
            z = x.replace(' ','')
            med_list = list(medicine.objects.values_list('name', flat=True))
            if x in med_list:
                return render(request,'Data\\drug_html_data\\medicine_data\\'+z+".html")
            else:
                messages.warning(request,"Medicine provided is invalid or may not be available in DB")
                return redirect('home')
    else:
        return HttpResponse("<h1>Error 404</h1>")
   
def Contact(request):

    if request.method == 'POST':
        First_name = request.POST['firstname']
        Last_name = request.POST['lastname']
        Email = request.POST['Email']
        Topic = request.POST['Topic']
        Issue = request.POST['subject']
        task = Contact_us(first_name = First_name,last_name = Last_name,Email = Email,topic = Topic,Issue = Issue)
        task.save()
        #print(task)
        messages.success(request,"We will reach you soon!")
        #print(First_name,Last_name,Email,Topic,Issue)
        return redirect('home')
    else:
        return HttpResponse("<h1>Error 404</h1>")

@login_required(login_url='home')
def Chatbot(request):
    if request.method == 'GET':
        return render(request,"HTML/Chatbot.html")
    else:
        return HttpResponse("<h1>Error 404</h1>")

def get_bot_response(request):
    if request.method == "GET":
        
        userText = request.GET['msg']
        return HttpResponse(str(getresponse(userText)))
        
    else:
        return HttpResponse("<h1>Error 404</h1>")
   
def check_token(request):
    if request.method == 'POST':
        ans = request.POST.get('token')
       
        print(ans,Random_token,type(ans),type(Random_token))
        if ans == Random_token:
            global user
            user = get_user_model().objects.create_user(username=Username,email=Email,password=password_1,first_name=First_name,last_name=Last_name)
            messages.success(request,"Successfully Sign In!")
            return redirect('home')    
        else:
            messages.error(request,'Token entered was incorrect. Please Sign In again')
            return redirect('home')

    else:
        return HttpResponse("<h1>ERROR 404</h1>")

