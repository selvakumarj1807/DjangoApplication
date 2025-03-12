from django.urls import path
from . import views

app_name = 'EnquiryManagement'

urlpatterns = [
    path('', views.home, name='home'),
    path('enquiryList/', views.enquiry_list, name='enquiry_list'),
]
