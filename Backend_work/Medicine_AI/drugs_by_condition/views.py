from django.shortcuts import render
import sys,os
from os import listdir
from django.contrib.auth.decorators import login_required
from os.path import isfile, join

@login_required(login_url='home')
def wounds(request):
    return render(request, "HTML/wounds.html")

@login_required(login_url='home')
def soft_tissue1(request):
    return render(request, "HTML/Soft_tissue_foreign_body.html")

@login_required(login_url='home')
def wound_infection(request):
    return render(request, "HTML/wound_infection.html")


@login_required(login_url='home')
def med_list(request):
    
    meds = []
    for f in listdir("Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\burns"):
        f=f.replace(".html","")
        meds.append(f)
    return render(request,"HTML/burns_med.html",{"list":meds})

# Create your views here.
def get_data(request):
    x = request.GET['term']
    print(x)
    z = x.replace(' ','')
    return render(request,'Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\burns\\'+z+".html")

@login_required(login_url='home')
def Pregnancy(request):
    return render(request,"HTML/Pregnancy_Care.html")

@login_required(login_url='home')
def PC1(request):
    return render(request,"HTML/breast-care-breastfeeding-mother.html")

@login_required(login_url='home')
def PC2(request):
    return render(request,"HTML/breast-Care-Non-Breast-Feeding-Woman.html")

@login_required(login_url='home')
def PC3(request):
    return render(request,"HTMl/Breastfeeding-and-Breast-Engorgement.html")

@login_required(login_url='home')
def PC4(request):
    return render(request,"HTML/ectopic-pregnancy.html")

@login_required(login_url='home')
def PC5(request):
    return render(request,"HTML/hyperthyroidism-in-pregnancy.html")

@login_required(login_url='home')
def PC6(request):
    return render(request,"HTML/Hypothyroidism-in-pregnancy.html")

@login_required(login_url='home')
def PC7(request):
    return render(request,"HTML/pregnancy-diet.html")

@login_required(login_url='home')
def PC8(request):
    return render(request,"HTML/pregnancy-induced-hypertension.html")

@login_required(login_url='home')
def Skin_infection(request):
    return render(request,"HTML/skin_infection.html")

@login_required(login_url='home')
def Bacterial_Inf(request):
    
    meds = []
    for f in listdir("Z:\\Backend_work\\Medicine_AI\\Data\\Skin_infections\\bacterial_infection_med"):
        f=f.replace(".html","")
        meds.append(f)
    return render(request,"HTML/Bacterial_Infection.html",{"list":meds})

def get_data_Bacterial(request):
    x = request.GET['term']
    print(x)
    z = x.replace(' ','')
    return render(request,'Z:\\Backend_work\\Medicine_AI\\Data\\Skin_infections\\bacterial_infection_med'+z+'.html')

@login_required(login_url='home')
def Soft_Tissue(request):
    meds = []
    for f in listdir("Z:\\Backend_work\\Medicine_AI\\Data\\Skin_infections\\soft_tissue_infection"):
        f=f.replace(".html","")
        meds.append(f)
    return render(request,"HTML/Soft_Tissue.html",{"list":meds})

def get_data_Tissue(request):
    x = request.GET['term']
    print(x)
    z = x.replace(' ','')
    return render(request,'Z:\\Backend_work\\Medicine_AI\\Data\\Skin_infections\\soft_tissue_infection\\'+z+'.html')
