from django.urls import path
from .views import add_patient, fetch_patients, get_personal_info, get_user_studies, login, register, save_personal_info, schedule_appointment, update_profile, change_password, save_ai_report, get_ai_reports, predict_scan, download_report, send_report_email

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('add-patient/', add_patient),
    path('patients/', fetch_patients),
    path('schedule-study/', schedule_appointment),
    path('user-studies/', get_user_studies),
    path('save-personal-info/', save_personal_info),
    path("get-personal-info/", get_personal_info),
    path('update-profile/', update_profile, name='update_profile'),
    path("change-password/", change_password),
    path("predict_scan/", predict_scan),
    path("save-ai-report/", save_ai_report),
    path("get-ai-reports/", get_ai_reports),
    path("send-report-email/", send_report_email),
]
