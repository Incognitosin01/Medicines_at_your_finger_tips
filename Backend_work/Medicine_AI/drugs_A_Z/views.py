from django.shortcuts import render
from Home.models import medicine
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Medicine_data
from Home.models import side_effect
from string import ascii_lowercase
# Create your views here.


import re
import speech_recognition as sr
import pyttsx3
from difflib import SequenceMatcher,get_close_matches
def pill_identifier(request):
    return render(request,"HTML/Pill_Identifier.html")

"""def drug_A(request):
        x = request.GET['term']
        if x=="A":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="B":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="C":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="D":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="E":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="F":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="G":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="H":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="I":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="J":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="K":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="L":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="M":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="N":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="O":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="P":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="Q":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="R":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="S":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="T":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="U":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="V":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="W":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="X":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="Y":
            return render(request,'HTML/Drug_A.html',{"val":x})
        elif x=="Z":
            return render(request,'HTML/Drug_A.html',{"val":x})"""


def drug_A(request):
    x=request.GET['term']
    di={}
    for i in ascii_lowercase:
        y=x+i
        z="type"+i
        qs = Medicine_data.objects.filter(alpha__contains = y).first()
        x1=len(qs.name_list)
        if(x1==0):
            d="disabled"
        else:
            d=" "
        di[z]=d
    di["val"]=x
    return render(request,"HTML/Drug_A.html",di)




def Drugs_alphabetically(request):
    x = request.GET['term']
    qs = Medicine_data.objects.filter(alpha__contains = x).first()
    x1=len(qs.name_list)
    print(x1)
    if(x1==1):
        disbl="disabled"
    else:
        disbl=" "
    print(disbl)
    return render(request,"HTML/Drugs_alpha_wise.html",{"list":qs.name_list,"val":x})

def get_data(request):
    x = request.GET['term']
    print(x)
    z = x.replace(' ','')
    if x!=("Your Medicines List Ends Here"):
        return render(request,'Data\\drug_html_data\\medicine_data\\'+z+".html")
    else:
        messages.warning(request,"No medicines to show")
        return render(request,'HTML/Pill_Identifier.html')

def Search_med(request) : 
    if request.method == 'GET':
        if 'term' in request.GET:
            qs = medicine.objects.filter(name__istartswith = request.GET['term'])
            names = []
            counter=10
            for i in qs:
                names.append(i.name)
                counter-=1
                if counter==0:
                    break
            return JsonResponse(names,safe=False)
        x = request.GET['query']
        z = x.replace(' ','')
        med_list = list(medicine.objects.values_list('name', flat=True))
        if x in med_list:
            return render(request,'Data\\drug_html_data\\medicine_data\\'+z+".html")
        else:
            messages.warning(request,"Medicine provided is invalid or may not avaialable in DB")
            return render(request,'HTML/Pill_Identifier.html')

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         print("Say that again please...")
#         return "None"
#     return query

    
def Phonetic_search(request):

    return render(request,'HTML/phonetic_search.html')

    
def speech_to_text(request):
    
    # get audio from the microphone
    global x_d
    x_d=['Not recognized!']
    if request.method == 'POST':
        data = request.POST.get('record')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)

        try:
            output = " " + r.recognize_google(audio)
        except sr.UnknownValueError:
            output = "Could not understand audio"
            print(output)
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)
            print(output)
        data = output
        global data_1
        
        data_1 = str(data)
        data_1 = data_1.replace(' ','')
        data_1 = data_1.capitalize()
        print(data_1)
        global med1,med2
        med1=list(side_effect.objects.values_list('name',flat=True))
        med2=list(medicine.objects.values_list('name',flat=True))
        ans = find_similar_word(data_1,med1+med2)
        ans = str(ans)
        return render(request,'HTML/phonetic_search.html',{'data':ans})

    
    else:
        return HttpResponse("<h1>ERROR 404</h1>")


def find_similar_word(s, kw,):
    
    global x_d
    x_d=['Not recognized!']
    if s in kw :
        x_d[0] = s
    else :
        x_d = get_close_matches(s, kw)
        if len(x_d)==0:
            x_d=['Not recognized!']
            
    return x_d[0]

def return_page(request):
    
    print(x_d)
    z = x_d[0].replace(' ','')
    if(x_d[0]=='Not recognized!'):
        return render(request,"E:\\Github_projects\\Medicines_at_your_finger_tips\\Backend_work\\Medicine_AI\\drugs_A_Z\\templates\\HTML\\phonetic_search.html")
    elif(x_d[0] not in med1):
        return render(request,"E:\\Github_projects\\Medicines_at_your_finger_tips\\Backend_work\\Medicine_AI\\drugs_A_Z\\templates\\HTML\\phonetic_search.html")


    else:
        return render(request,"Data\\drug_html_data\\medicine_data\\"+z+".html")
        

def return_side_effects(request):
    z=x_d[0]
    
    if(x_d[0]=='Not recognized!'):
        return render(request,"E:\\Github_projects\\Medicines_at_your_finger_tips\\Backend_work\\Medicine_AI\\drugs_A_Z\\templates\\HTML\\phonetic_search.html")
    elif(z not in med2):

        return render(request,"E:\\Github_projects\\Medicines_at_your_finger_tips\\Backend_work\\Medicine_AI\\drugs_A_Z\\templates\\HTML\\phonetic_search.html")

    
    else:
        z = x_d[0].replace('-',' ')
        return render(request,"Data\\side_effects2\\"+z+".html")
            




