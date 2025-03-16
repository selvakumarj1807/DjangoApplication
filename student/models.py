from django.db import models

# Create your models here.

class StudentInterviewSchedule(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    round = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    student_mobile  = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"