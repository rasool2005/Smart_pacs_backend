from django.contrib import admin
from .models import AIChat, AIReport, Patient, PatientStudy, PersonalInfo, User, PasswordResetOTP, ScanPrediction

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(PatientStudy)
admin.site.register(PersonalInfo)
admin.site.register(AIReport)
admin.site.register(PasswordResetOTP)
admin.site.register(ScanPrediction)
admin.site.register(AIChat)
