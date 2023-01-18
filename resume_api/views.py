from django.shortcuts import render
import boto3

# Create your views here.
from rest_framework import generics, status
from .serializers import ResumeSerializer
from .models import Resume
from rest_framework.parsers import  MultiPartParser, FormParser
from rest_framework.response import Response



class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all().order_by('id')
    serializer_class = ResumeSerializer
    # everything below is taken from here to get django to process the file upload
    # https://stackoverflow.com/questions/71241619/no-file-was-submitted-error-when-trying-to-do-an-axios-post-between-react-and-dj
    # MultiPartParser handles file uploads in addition to static form data
    parser_classes = (MultiPartParser, FormParser)

    def post (self, request, *args, **kwargs):
        fileSerializer = ResumeSerializer(data=request.data)
        if fileSerializer.is_valid():
            fileSerializer.save()
            return Response(fileSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all().order_by('id')
    serializer_class = ResumeSerializer

