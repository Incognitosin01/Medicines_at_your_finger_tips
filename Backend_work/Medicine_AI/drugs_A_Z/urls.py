from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path("Pill_identifier/", views.pill_identifier, name="Pill_Identifier"),
    path('Search_med/',views.Search_med,name='search_med'),
    path('Drug_A/',views.drug_A,name="Drug_A"),
    path('Drugs_Alpha_Wise/',views.Drugs_alphabetically,name="Drugs_Alpha_Wise"),
    path('Medicine/',views.get_data,name="medicine_data"),
    path("phonetic_search/",views.Phonetic_search,name='Phonetic_search'),
    path("speech_to_text/",views.speech_to_text,name='speech_to_text'),
    path("voice_data/",views.return_page,name='voice_data')
]
