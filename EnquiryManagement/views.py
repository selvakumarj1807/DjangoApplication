from django.shortcuts import render

# Create your views here.

from StudentEnquiry.models import StudentEnquiry  # Import your model

def home(request):
    return render(request, 'EnquiryManagementIndex.html')


def enquiry_list(request):
    enquiries = StudentEnquiry.objects.all()  # Fetch all entries
    return render(request, 'EnquiryList.html', {'enquiries': enquiries})