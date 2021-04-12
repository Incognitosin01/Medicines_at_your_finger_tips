from django.contrib import admin
from .models import Contact_us,medicine,side_effect
# Register your models here.

admin.site.register(Contact_us)
admin.site.register(medicine)
admin.site.register(side_effect)