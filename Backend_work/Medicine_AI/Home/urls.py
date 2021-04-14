from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('about',views.about,name='about'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('drugs_a_z',views.drug_A_Z,name='drugs_A_Z'),
    path('drugs_by_cond',views.drug_cond,name='drugs_by_cond'),
    path('side_effects',views.side_effects,name='side_effects'),
    path('first_aid',views.first_aid,name='first_aid'),
    path('symptom_checker',views.symptom_checker,name='Symptom_checker'),
    path('My_med_list',views.med_list,name='My_med_list'),
    path("sign_up",views.sign_up,name='sign_up'),
    path('login',views.handle_login,name='login'),
    path('logout',views.handle_logout,name='logout'),
    path('search',views.search,name='search'),
    path('contact',views.Contact,name='contact'),
    path('Chatbot',views.Chatbot,name='chatbot'),
    path('get',views.get_bot_response,name="response"),
    path('get_token',views.check_token,name='get_token'),
    path('get_bot',views.get_data_bot,name='get_data_bot')
    
]
