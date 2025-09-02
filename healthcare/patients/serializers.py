from rest_framework import serializers
from .models import Patient, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['added_by', 'created_at']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.__str__', read_only=True)
    doctor_name = serializers.CharField(source='doctor.__str__', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_name', 'doctor_name', 'assigned_at']
        read_only_fields = ['assigned_at']