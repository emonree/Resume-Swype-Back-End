from django.shortcuts import render
import boto3

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


# tried to copy the code from the flask app version in the documentation: https://devcenter.heroku.com/articles/s3-upload-python
# don't know if it works because the /api/resumes/upload URL returns a 500 error status
class ResumeUpload:
    def sign_s3(file):
        S3_BUCKET = "resumeswypestorage"

        file_name = request.args.get('file_name')
        file_type = request.args.get('file_type')

        s3 = boto3.client('s3')

        presigned_post = s3.generate_presigned_post(
            Bucket = S3_BUCKET,
            Key = file_name,
            Fields = {"acl": "public-read", "Content-Type": file_type},
            Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
            ],
            ExpiresIn = 3600
        )

        return json.dumps({
            'data': presigned_post,
            'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
        })