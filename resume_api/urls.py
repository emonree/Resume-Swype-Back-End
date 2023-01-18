from django.urls import path
from . import views

urlpatterns = [
    path('api/resumes', views.ResumeList.as_view(), name='resume_list'),
    path('api/resumes/<int:pk>', views.ResumeDetail.as_view(), name='resume_detail'), 
]