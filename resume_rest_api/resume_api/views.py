from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ResumeSerializer
from .models import Resume

class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all().order_by('id')
    serializer_class = ResumeSerializer

class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all().order_by('id')
    serializer_class = ResumeSerializer