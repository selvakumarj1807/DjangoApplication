from django.db import models

# Create your models here.

class StudentEnquiry(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    education = models.CharField(max_length=100)
    year_passout = models.CharField(max_length=10)
    required_course = models.CharField(max_length=100)
    placement = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    profession = models.CharField(max_length=10, choices=[('IT', 'IT'), ('NON-IT', 'Non-IT')])
    company_name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    pf = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    uan_no = models.CharField(max_length=20, blank=True, null=True)
    form_16 = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    pan_aadhar = models.CharField(max_length=20, blank=True, null=True)
    refer_by = models.CharField(max_length=100, blank=True, null=True)
    referer_mbl = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
