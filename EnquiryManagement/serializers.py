from rest_framework import serializers
from StudentEnquiry.models import StudentEnquiry
from student.models import StudentInterviewSchedule

class StudentEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'  # Include all fields

class StudentInterviewSheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInterviewSchedule
        fields = '__all__'  # Include all fields
