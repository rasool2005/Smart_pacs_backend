from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hospital_id = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient_name
    
class PatientStudy(models.Model):
    user_id = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    study_type = models.CharField(max_length=100)
    study_date = models.DateField()
    study_time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.patient_name} - {self.study_type}"

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)

    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class AIReport(models.Model):
    EXAM_CHOICES = [
        ('XRAY', 'X-Ray'),
        ('CT', 'CT Scan'),
        ('MRI', 'MRI'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    examination_type = models.CharField(max_length=20, choices=EXAM_CHOICES)

    confidence_score = models.FloatField()
    confidence_level = models.CharField(max_length=50)

    finding_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    observation = models.TextField()
    severity = models.CharField(max_length=100)

    impression = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.examination_type} - {self.finding_name}"
