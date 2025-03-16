from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import StudentInterviewSchedule
from .serializers import StudentInterviewSheduleSerializer

# Create your views here.
def home(request):
    return render(request, 'StudentIndex.html')

def interviewShedule(request):
    return render(request, 'interviewSchduleForm.html')

@csrf_exempt  # Exempt CSRF for API requests
def interview_submit_form(request):
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
        serializer = StudentInterviewSheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # API Response for Postman
            if request.content_type == 'application/json':
                return JsonResponse({"message": "Student interviewSchduleForm Submitted Successfully!"}, status=201)

            # Redirect for HTML form submissions
            return redirect('student:home')

        # Handle errors for both cases
        if request.content_type == 'application/json':
            return JsonResponse(serializer.errors, status=400)

        return render(request, 'interviewSchduleForm.html', {'errors': serializer.errors})

    # For non-POST requests (e.g., GET)
    return render(request, 'interviewSchduleForm.html')