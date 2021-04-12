from django.urls import path
from .import views

urlpatterns = [
    path('Search_side_effect/',views.Search,name='Search_side_effect'),
    
    path('Drug_A_side_effects/',views.drug_A1,name="Drug_A_side_effects"),
    path('side_effects_alpha/',views.drugs_alphabetically,name="side_effects_alpha"),
    path('Side_Medicine/',views.Get_data,name="side_effect_data"),
]
