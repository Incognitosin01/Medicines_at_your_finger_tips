from django.db import models

# Create your models here.
class Med_list(models.Model):

    Medication_Name = models.CharField(max_length=500,null=False)
    Dosage = models.CharField(max_length=500,null=False)
    Instructions = models.CharField(max_length=500,null=False)

    def __str__(self):
        return str(self.Medication_Name)

