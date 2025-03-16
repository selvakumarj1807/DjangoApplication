from django.utils.timezone import localdate
from django.shortcuts import render
from django.http import JsonResponse
from StudentEnquiry.models import StudentEnquiry
from student.models import StudentInterviewSchedule  # Import your model

def home(request):
    return render(request, 'EnquiryManagementIndex.html')

# Enquiry List View (API + Frontend)
def enquiry_list(request):
    enquiries = list(StudentEnquiry.objects.all().order_by('-created_at').values())  # Order by created_at descending
    enquiry_count = StudentEnquiry.objects.count()

    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({"count": enquiry_count, "enquiries": enquiries}, safe=False)

    return render(request, 'EnquiryList.html', {'enquiries': enquiries})

# Interview List View (API + Frontend)
def interview_list(request):
    today = localdate().strftime("%Y-%m-%d")  # Convert today's date to string format

    # Fetch all interviews
    interviews = list(StudentInterviewSchedule.objects.all().values())

    # Filter today's interviews by manually comparing string dates
    today_interviews = [interview for interview in interviews if interview['date'] == today]
    today_interview_count = len(today_interviews)  # Count today's interviews

    # If the request is from Postman (API request)
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            "count": len(interviews),
            "interviews": interviews,
            "today_count": today_interview_count,
            "today_interviews": today_interviews
        }, safe=False)

    # Else, render the HTML page (Frontend)
    return render(request, 'InterviewList.html', {
        'interviews': interviews,
        'today_date': today,
        'today_interview_count': today_interview_count,
        "today_interviews": today_interviews
    })