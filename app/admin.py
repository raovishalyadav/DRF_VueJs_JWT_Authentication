from django.contrib import admin
from .models import Apicrud

@admin.register(Apicrud)

class admin_Apicrud(admin.ModelAdmin):
    list_display = ['first', 'second','third','fourth','fifth','sixth','seventh','eight','nine']


    