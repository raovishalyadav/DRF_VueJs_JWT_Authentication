from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Apicrud
from .serializers import serializers_Apicrud

class cruddata(ModelViewSet):
    queryset = Apicrud.objects.all()
    serializer_class = serializers_Apicrud
    