from django.shortcuts import render,HttpResponse,render,redirect
from django.contrib import messages
from .models import Med_list
from Home.views import med_list
# Create your views here.


def Create_data(request):
    if request.method == "POST":
        Medication_Name = request.POST['Medication_Name']
        Dosage = request.POST['Dosage']
        Instructions = request.POST['Instructions']
        
        x=Med_list(Medication_Name=Medication_Name,Dosage=Dosage,Instructions=Instructions)
        x.save()
        all_medications = Med_list.objects.all()
        return redirect('My_med_list')

def delete_data(request,id):
    if request.method == "POST":
        x = Med_list.objects.get(pk=id)
        x.delete()
        return redirect('My_med_list')
