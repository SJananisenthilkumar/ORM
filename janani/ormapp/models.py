from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    email=models.EmailField()
    age=models.CharField(max_length=100)

class FootballAdmin(admin.ModelAdmin):
    list_display=['name','address','mobileno','email','age']
