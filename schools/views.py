from django.shortcuts import render
from rest_framework import generics
from .models import NSWSchool
from .serializers import NSWSchoolSerializer

class NSWSchoolList(generics.ListCreateAPIView):
    queryset = NSWSchool.objects.all()
    serializer_class = NSWSchoolSerializer
