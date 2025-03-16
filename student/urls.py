from django.urls import path
from . import views

app_name = 'student'  # Namespace for app

urlpatterns = [
    path('', views.home, name='home'),
    path('interviewShedule/', views.interviewShedule, name='interviewShedule'),
    path('interview-submit-form/', views.interview_submit_form, name='interview_submit_form'),
]
