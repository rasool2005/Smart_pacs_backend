from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .serializers import (
    FetchPatientSerializer,
    LoginSerializer,
    PatientStudySerializer,
    PersonalInfoSerializer,
    RegisterSerializer,
    PatientSerializer,
    StudySerializer,
    ChangePasswordSerializer,
    AIReportSerializer,
)

from .models import Patient, PatientStudy, PersonalInfo, User, AIReport

import os
import os
import io
import numpy as np
#import tensorflow as tf
from PIL import Image
from django.conf import settings

# ===========================
# LOAD AI MODEL
# ===========================

try:
    model_path = os.path.join(settings.BASE_DIR, "scan_model.h5")
    model = tf.keras.models.load_model(model_path)
    print("AI Model loaded successfully")
except Exception as e:
    print("Model loading failed:", e)
    model = None

class_names = ["CT", "MRI", "XRAY"]

# ===========================
# AUTH APIs
# ===========================

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"status": "success", "message": "Registration successful"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {"status": "error", "message": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data["user"]

        return Response({
            "status": "success",
            "message": "Login successful",
            "user": {
                "user_id": user.id,
                "name": user.name,
                "email": user.email,
                "hospital_id": user.hospital_id
            }
        }, status=status.HTTP_200_OK)

    return Response({
        "status": "error",
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# ===========================
# PATIENT APIs
# ===========================

@api_view(['POST'])
def add_patient(request):
    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        patient = serializer.save()
        return Response({
            "status": "success",
            "patient_id": patient.id,
            "message": "Patient added successfully"
        })

    return Response({
        "status": "error",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch_patients(request):
    patients = Patient.objects.all().order_by('-id')

    if patients.exists():
        serializer = FetchPatientSerializer(patients, many=True)
        return Response({
            "status": "success",
            "count": patients.count(),
            "patients": serializer.data
        })

    return Response({
        "status": "error",
        "message": "No patients found"
    })


# ===========================
# STUDY / APPOINTMENT APIs
# ===========================

@api_view(['POST'])
def schedule_appointment(request):
    serializer = PatientStudySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(status="pending")
        return Response({
            "status": "success",
            "message": "Appointment scheduled successfully",
            "study_status": "pending"
        })

    return Response({
        "status": "error",
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_user_studies(request):
    user_id = request.data.get("user_id")

    if not user_id:
        return Response({
            "status": "error",
            "message": "user_id is required"
        }, status=status.HTTP_400_BAD_REQUEST)

    studies = PatientStudy.objects.filter(
        user_id=user_id
    ).order_by("-id")

    serializer = StudySerializer(studies, many=True)

    return Response({
        "status": "success",
        "studies": serializer.data,
        "counts": {
            "pending": studies.filter(status="pending").count(),
            "confirmed": studies.filter(status="confirmed").count()
        }
    })


# ===========================
# PROFILE APIs
# ===========================

@api_view(['POST'])
def save_personal_info(request):
    serializer = PersonalInfoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": "success",
            "message": "Personal information saved successfully"
        })

    return Response({
        "status": "error",
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_personal_info(request):
    user_id = request.data.get("user_id")

    if not user_id:
        return Response({
            "status": "error",
            "message": "user_id is required"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({
            "status": "error",
            "message": "User not found"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        personal_info = PersonalInfo.objects.get(id=user_id)
        serializer = PersonalInfoSerializer(personal_info)

        return Response({
            "status": "success",
            "data": serializer.data
        })

    except PersonalInfo.DoesNotExist:
        return Response({
            "status": "error",
            "message": "Personal information not found"
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_profile(request):
    user_id = request.data.get("user_id")

    if not user_id:
        return Response({
            "status": "error",
            "message": "user_id is required"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({
            "status": "error",
            "message": "User not found"
        }, status=status.HTTP_404_NOT_FOUND)

    profile, _ = PersonalInfo.objects.get_or_create(user=user)

    serializer = PersonalInfoSerializer(
        profile,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": "success",
            "message": "Profile updated successfully"
        })

    return Response({
        "status": "error",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": "success",
            "message": "Password updated successfully"
        })

    return Response({
        "status": "error",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

# ===========================
# AI REPORT APIs (without prediction)
# ===========================

@api_view(['POST'])
def save_ai_report(request):
    user_id = request.data.get("user_id")

    if not user_id:
        return Response({"status": "error", "message": "user_id is required"}, status=400)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"status": "error", "message": "User not found"}, status=404)

    serializer = AIReportSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response({"status": "success", "message": "AI Report saved successfully"}, status=201)

    return Response({"status": "error", "errors": serializer.errors}, status=400)


@api_view(['GET'])
def get_ai_reports(request):
    user_id = request.GET.get("user_id")

    if not user_id:
        return Response({"status": "error", "message": "user_id is required"}, status=400)

    reports = AIReport.objects.filter(user_id=user_id).order_by("-id")
    serializer = AIReportSerializer(reports, many=True)

    return Response({
        "status": "success",
        "count": reports.count(),
        "reports": serializer.data
    })


@api_view(['POST'])
def predict_scan(request):
    try:
        if "file" not in request.FILES:
            return Response(
                {"status": "error", "message": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES["file"]

        if file.name == "":
            return Response(
                {"status": "error", "message": "Empty filename"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Process image
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        img = img.resize((224, 224))

        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        if model is None:
            return Response(
                {"status": "error", "message": "Model not loaded"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Prediction
        prediction = model.predict(img_array)[0]
        confidence = float(np.max(prediction))
        predicted_index = int(np.argmax(prediction))
        predicted_class = class_names[predicted_index]

        # Dynamic Findings
        findings = []

        if predicted_class == "CT":
            findings.append({
                "title": "Pulmonary Nodule",
                "location": "Upper Left Lobe",
                "description": "A 6mm well-defined nodule observed. Recommend follow-up CT in 6 months to assess stability.",
                "confidence": round(confidence * 94.2, 1),
                "severity": "Low"
            })

        elif predicted_class == "MRI":
            findings.append({
                "title": "Abnormal Signal Intensity",
                "location": "Occipital Region",
                "description": "Hyperintense signal detected on T2-weighted images. Urgent radiologist review recommended.",
                "confidence": round(confidence * 89.5, 1),
                "severity": "High"
            })

        elif predicted_class == "XRAY":
            findings.append({
                "title": "Pleural Effusion",
                "location": "Left Costophrenic Angle",
                "description": "Blunting of the costophrenic angle suggesting mild fluid accumulation in the pleural space.",
                "confidence": round(confidence * 76.3, 1),
                "severity": "Moderate"
            })

        # Confidence Level
        if confidence > 0.95:
            level = "Very High"
        elif confidence > 0.85:
            level = "High"
        elif confidence > 0.70:
            level = "Medium"
        else:
            level = "Low"

        warning = (
            "Low AI confidence. Professional review recommended."
            if confidence < 0.75
            else "AI analysis complete."
        )

        return Response({
            "status": "success",
            "scan_type": predicted_class,
            "confidence_score": round(confidence * 100, 2),
            "confidence_level": level,
            "message": warning,
            "findings": findings
        })

    except Exception as e:
        return Response({
            "status": "error",
            "message": "Prediction failed",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def send_report_email(request):
    """Send AI report via email to patient"""
    try:
        patient_email = request.data.get("patient_email")
        report_id = request.data.get("report_id")
        
        if not patient_email or not report_id:
            return Response({
                "status": "error",
                "message": "patient_email and report_id are required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the report
        report = AIReport.objects.get(id=report_id)
        
        # Prepare email content
        subject = f"SmartPACS - {report.examination_type} Report"
        
        email_body = f"""
Dear Patient,

Your AI analysis report is ready for review.

Report Details:
================
Examination Type: {report.examination_type}
Finding: {report.finding_name}
Location: {report.location}
Severity: {report.severity}

AI Confidence Score: {report.confidence_score}%
Confidence Level: {report.confidence_level}

Observation:
{report.observation}

Impression:
{report.impression}

Generated on: {report.created_at.strftime('%Y-%m-%d %H:%M:%S')}

Please consult with your physician for further guidance.

Best regards,
SmartPACS Analysis System
"""
        
        # Send email
        send_mail(
            subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [patient_email],
            fail_silently=False,
        )
        
        return Response({
            "status": "success",
            "message": "Report sent to email successfully"
        }, status=status.HTTP_200_OK)
        
    except AIReport.DoesNotExist:
        return Response({
            "status": "error",
            "message": "Report not found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({
            "status": "error",
            "message": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)