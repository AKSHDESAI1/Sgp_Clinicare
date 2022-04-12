from pyexpat import model
from django.db import models

# Create your models here.
class Information(models.Model):
    GENDER_CHOICES = (
        ('male1', 'Male'),
        ('female1', 'Female')
    )
    BLOOD_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No')
    )
    DIA_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No')
    )
    username=models.CharField(max_length=30)
    gender1 = models.CharField(max_length=7,choices=GENDER_CHOICES)
    date1 = models.DateField()
    blood1 = models.CharField(max_length=7,choices=BLOOD_CHOICES)
    dia1 = models.CharField(max_length=7,choices=DIA_CHOICES)
    medical = models.TextField()
    alergies = models.TextField()
    
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    subject = models.TextField()