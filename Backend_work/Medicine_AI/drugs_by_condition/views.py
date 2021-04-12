from django.shortcuts import render
import sys,os
from os import listdir
from os.path import isfile, join

def wounds(request):
    return render(request, "Z:\\Backend_work\\Medicine_AI\\drugs_by_condition\\templates\\HTML\\wounds.html")

def soft_tissue1(request):
    return render(request, "Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\Soft_tissue_foreign_body.html")
def wound_infection(request):
    return render(request, "Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\wound_infection.html")



def med_list(request):
    
    meds = []
    for f in listdir("Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\burns"):
        f=f.replace(".html","")
        meds.append(f)
    return render(request,"Z:\\Backend_work\\Medicine_AI\\drugs_by_condition\\templates\\HTML\\burns_med.html",{"list":meds})

# Create your views here.
def get_data(request):
    x = request.GET['term']
    print(x)
    z = x.replace(' ','')
    return render(request,'Z:\\Backend_work\\Medicine_AI\\Data\\wounds\\burns\\'+z+".html")




# Create your views here.
def Pregnancy(request):
    return render(request,"HTML/Pregnancy_Care.html")

def PC1(request):
    return render(request,"HTML/breast-care-breastfeeding-mother.html")

def PC2(request):
    return render(request,"HTML/breast-Care-Non-Breast-Feeding-Woman.html")

def PC3(request):
    return render(request,"HTMl/Breastfeeding-and-Breast-Engorgement.html")

def PC4(request):
    return render(request,"HTML/ectopic-pregnancy.html")

def PC5(request):
    return render(request,"HTML/hyperthyroidism-in-pregnancy.html")

def PC6(request):
    return render(request,"HTML/Hypothyroidism-in-pregnancy.html")

def PC7(request):
    return render(request,"HTML/pregnancy-diet.html")

def PC8(request):
    return render(request,"HTML/pregnancy-induced-hypertension.html")

def Skin_infection(request):
    return render(request,"HTML/skin_infection.html")

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
