from django.urls import path
from . import views

app_name = 'StudentEnquiry'

urlpatterns = [
    path('', views.home, name='home'),
    path('enquiryForm/', views.enquiry_form, name='enquiry_form'),
    # Single route for both form and Postman requests
    path('submit-enquiry/', views.submit_enquiry, name='submit-enquiry'),]
