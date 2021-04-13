from django.shortcuts import render
from Home.models import side_effect
from .models import side_effects_data
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from string import ascii_lowercase, ascii_uppercase
# Create your views here.

def Search(request) : 
    if request.method == 'GET':
        if 'term' in request.GET:
            qs = side_effect.objects.filter(name__istartswith = request.GET['term'])
            #print(side_effect.objects.all())
            names = []
            counter=5
            for i in qs:
                names.append(i.name)
                counter-=1
                if counter==0:
                    break
            return JsonResponse(names,safe=False)
        x = request.GET['query']
        z = x.replace('-side-effect','')
        med_list = list(side_effect.objects.values_list('name', flat=True))
        if x in med_list:
            return render(request,'Data\\side_effects2\\'+z+".html")
        else:
            print("hello")
            messages.warning(request,"Medicine provided is invalid or may not avaialable in DB")
            return redirect('side_effects')
'''def drug_A1(request):
        x = request.GET['term']
        if x=="A":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="B":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="C":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="D":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="E":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="F":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="G":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="H":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="I":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="J":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="K":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="L":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="M":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="N":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="O":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="P":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="Q":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="R":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="S":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="T":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="U":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="V":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="W":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="X":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="Y":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})
        elif x=="Z":
            return render(request,'HTML/Drug_A_side_effects.html',{"val":x})'''


def drug_A1(request):
    x=request.GET['term']
    di={}
    for i in ascii_lowercase:
        y=x+i
        z="type"+i
        qs = side_effects_data.objects.filter(alpha__contains = y).first()
        x1=len(qs.name_list)
        if(x1==0):
            d="disabled"
        else:
            d=" "
        di[z]=d
    di["val"]=x
    return render(request,"HTML/Drug_A_side_effects.html",di)

def drugs_alphabetically(request):
    x = request.GET['term']
    qs = side_effects_data.objects.filter(alpha__contains = x).first()
    print(qs)
    return render(request,"HTML/side_effects_alpha.html",{"list":qs.name_list,"val":x})

def Get_data(request):
    x = request.GET['term']
    print(x)
    
    z= x.replace('-side-effect','')
    if x!=("Your Medicines List Ends Here"):
        return render(request,'Data\\side_effects2\\'+z+".html")
    else:
        messages.warning(request,"No medicines to show")
        return render(request,'HTML/side_effects.html')