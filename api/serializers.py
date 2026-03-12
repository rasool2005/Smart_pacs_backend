from rest_framework import serializers
from .models import PatientStudy, PersonalInfo, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Patient,PersonalInfo,AIReport,ScanPrediction
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re   # 🔥 ADD THIS LINE

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'hospital_id', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Check hashed password
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid email or password")

        data["user"] = user
        return data

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_name",
            "dob",
            "phone_number",
            "address",
            "email",
            "blood_type",
            "allergies"
        ]

    # Required field validation
    def validate(self, data):
        if not data.get("patient_name"):
            raise serializers.ValidationError(
                {"patient_name": "Patient name is required"}
            )

        if not data.get("dob"):
            raise serializers.ValidationError(
                {"dob": "DOB is required"}
            )

        return data

    # Phone validation
    def validate_phone_number(self, value):
        if value and len(value) < 10:
            raise serializers.ValidationError(
                "Invalid phone number length"
            )
        return value

    # Email validation
    def validate_email(self, value):
        if value:
            try:
                validate_email(value)
            except ValidationError:
                raise serializers.ValidationError(
                    "Invalid email address"
                )
        return value
    
class FetchPatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(source='id')

    class Meta:
        model = Patient
        fields = [
            "patient_id",
            "patient_name",
            "dob",
            "phone_number",
            "address",
            "email",
            "blood_type",
            "allergies"
        ]
        read_only_fields = fields

class PatientStudySerializer(serializers.ModelSerializer):

    study_time = serializers.TimeField(
        input_formats=["%H:%M", "%I:%M %p"]  # 24hr and AM/PM both allowed
    )

    class Meta:
        model = PatientStudy
        fields = [
            "user_id",
            "patient_name",
            "study_type",
            "study_date",
            "study_time",
            "note"
        ]

    def validate(self, data):
        # Check required fields
        required_fields = [
            "user_id",
            "patient_name",
            "study_type",
            "study_date",
            "study_time"
        ]

        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(
                    {field: "This field is required."}
                )

        # Check if patient exists
        if not Patient.objects.filter(
            patient_name=data["patient_name"]
        ).exists():
            raise serializers.ValidationError(
                {"patient_name": "Patient not found. Please add patient first."}
            )

        return data
    
class StudySerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientStudy
        fields = [
            "id",
            "patient_name",
            "study_type",
            "study_date",
            "study_time",
            "note",
            "status",
        ]

class PersonalInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PersonalInfo
        fields = [
            "user_id",
            "first_name", 
            "last_name",
            "email", 
            "phone_number", 
            "date_of_birth",
            "street_address", 
            "city", 
            "state", 
            "zip_code"
        ]

    def validate(self, data):
        required_fields = [
            "user_id", "first_name", "last_name",
            "email", "phone_number", "date_of_birth",
            "street_address", "city", "state", "zip_code"
        ]

        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(
                    {field: "This field is required"}
                )

        # Verify user exists
        user_id = data.get("user_id")
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"user_id": "User does not exist"}
            )

        return data

    def validate_phone_number(self, value):
        if not re.match(r'^[0-9]{10}$', value):
            raise serializers.ValidationError(
                "Invalid phone number"
            )
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        return PersonalInfo.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            instance.user_id = user_id
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user_id = data.get("user_id")
        current_password = data.get("current_password")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "User not found"})

        if not check_password(current_password, user.password):
            raise serializers.ValidationError(
                {"current_password": "Current password is incorrect"}
            )

        if new_password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match"}
            )

        # Password Strength Rules
        if len(new_password) < 8:
            raise serializers.ValidationError(
                {"new_password": "Minimum 8 characters required"}
            )

        if not re.search(r'[A-Z]', new_password):
            raise serializers.ValidationError(
                {"new_password": "Must contain uppercase letter"}
            )

        if not re.search(r'[a-z]', new_password):
            raise serializers.ValidationError(
                {"new_password": "Must contain lowercase letter"}
            )

        if not re.search(r'[0-9]', new_password):
            raise serializers.ValidationError(
                {"new_password": "Must contain a number"}
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', new_password):
            raise serializers.ValidationError(
                {"new_password": "Must contain special character"}
            )

        data["user"] = user
        return data

    def save(self):
        user = self.validated_data["user"]
        user.password = make_password(self.validated_data["new_password"])
        user.save()
        return user
class AIReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIReport
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']


from rest_framework import serializers


class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField()

class ScanPredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScanPrediction
        fields = "__all__"