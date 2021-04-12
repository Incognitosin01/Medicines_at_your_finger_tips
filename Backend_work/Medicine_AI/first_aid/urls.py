from django.urls import path
from .import views

urlpatterns = [
    path("accident_n_emergencies/",views.acc_emerg,name="accident_n_emergency"),
    path("first_aid_info/",views.info,name="first_aid_info"),
    path("first_aid_kit/",views.kit,name="first_aid_kit"),
    path("first_aid_gloss/",views.gloss,name="first_aid_gloss")
]
