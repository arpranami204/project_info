from django.db import models
from django.conf import settings


# Create your models here.

class Doctor(models.Model):
    # id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    experience_years = models.IntegerField()
    consultation_fee = models.FloatField()
    is_available = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateField()
    image = models.FileField(upload_to='doctor_image')


    def __str__(self):
        return self.full_name


    
class Caretaker(models.Model):
    # id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    experience_years = models.IntegerField()
    service_charge = models.FloatField()
    availability_status = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    image = models.FileField(upload_to='caretaker_image')


    def __str__(self):
        return self.full_name


    
class ServiceApproval(models.Model):
    # id = models.AutoField(primary_key=True)
    booking = models.CharField(max_length=100)
    approved_by = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=50)
    approval_date = models.DateField()
    remarks = models.TextField()


    def __str__(self):
        return f"Approval for {self.booking}"


    
class AdminReport(models.Model):
    # id = models.AutoField(primary_key=True)
    total_users = models.IntegerField()
    total_bookings = models.IntegerField()
    total_payments = models.FloatField()
    total_emergencies = models.IntegerField() 
    report_date = models.DateField()
    generated_at = models.DateTimeField()

    def __str__(self):
        return f"Report - {self.report_date}" 


