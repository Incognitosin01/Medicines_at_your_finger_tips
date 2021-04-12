from django.db import models
from django_mysql.models import ListTextField
# Create your models here.
class side_effects_data(models.Model):

    alpha = models.CharField(max_length=2,primary_key=True)
    name_list = ListTextField(
        base_field=models.CharField(max_length=100),
        size=400,
        
    )