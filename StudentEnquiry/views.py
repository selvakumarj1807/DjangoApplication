from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # For API requests via Postman
from django.utils.decorators import method_decorator
from .models import StudentEnquiry
from .serializers import StudentEnquirySerializer
import json  # For JSON parsing in API requests

def home(request):
    return render(request, 'StudentEnquiryIndex.html')

def enquiry_form(request):
    return render(request, 'enquiryForm.html')

# Function-based view for handling both form submission and API requests
@csrf_exempt  # Exempt CSRF for API requests
def submit_enquiry(request):
    if request.method == 'POST':
        # Handle JSON data (for Postman API requests)
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)  # Parse JSON data
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
        # Handle HTML form submissions
        else:
            data = request.POST  # Standard HTML form data

        # Use serializer for data validation
        serializer = StudentEnquirySerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # API Response for Postman
            if request.content_type == 'application/json':
                return JsonResponse({"message": "Student Enquiry Submitted Successfully!"}, status=201)

            # Redirect for HTML form submissions
            return redirect('StudentEnquiry:home')

        # Handle errors for both cases
        if request.content_type == 'application/json':
            return JsonResponse(serializer.errors, status=400)

        return render(request, 'enquiryForm.html', {'errors': serializer.errors})

    # For non-POST requests (e.g., GET)
    return render(request, 'enquiryForm.html')
