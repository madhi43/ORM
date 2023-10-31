from django.db import models
from django.contrib import admin
class Football (models.Model):
    jerseyno=models.CharField(max_length=20,help_text="jerseyno")
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    age=models.IntegerField()
    YOE=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('jerseyno','name','country','age','YOE')