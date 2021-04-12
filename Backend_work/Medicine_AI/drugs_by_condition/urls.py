from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('wounds',views.wounds,name="wounds"),
    path('burns_list',views.med_list,name="burns_list"),
    path('burns_data',views.get_data,name="burns_data"),
    path('soft_tissue1',views.soft_tissue1,name="soft_tissue1"),
    path('wound_infection',views.wound_infection,name="wound_infection"),
    path("Pregnancy_Care",views.Pregnancy,name="Pregnancy_Care"),
    path("breast-care-breastfeeding-mother",views.PC1,name="PC1"),
    path("breast-Care-Non-Breast-Feeding-Woman",views.PC2,name="PC2"),
    path("Breastfeeding-and-Breast-Engorgement",views.PC3,name="PC3"),
    path("ectopic-pregnancy",views.PC4,name="PC4"),
    path("hyperthyroidism-in-pregnancy",views.PC5,name="PC5"),
    path("Hypothyroidism-in-pregnancy",views.PC6,name="PC6"),
    path("pregnancy-diet",views.PC7,name="PC7"),
    path("pregnancy-induced-hypertension",views.PC8,name="PC8"),
    path("skin_infection",views.Skin_infection,name="skin_infection"),
    path("Bacterial_Inf",views.Bacterial_Inf,name="Bacterial"),
    path("Soft_Tissue",views.Soft_Tissue,name="Soft"),
    path("Bacterial_Med",views.get_data_Bacterial,name="Bacteria"),
    path("Soft_Tissue_Med",views.get_data_Tissue,name="Soft_Tissue"),
]
