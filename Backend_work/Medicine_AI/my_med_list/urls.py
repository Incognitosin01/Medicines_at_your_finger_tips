from django.urls import path
from .import views
urlpatterns = [
    path('Myy_med_list',views.Create_data,name='Myy_med_list'),
    path('delete_data/<int:id>',views.delete_data,name="delete_data")
]

