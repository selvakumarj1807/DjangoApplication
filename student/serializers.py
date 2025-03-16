from rest_framework import serializers
from .models import StudentInterviewSchedule

class StudentInterviewSheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInterviewSchedule
        fields = '__all__'  # Includes all model fields
