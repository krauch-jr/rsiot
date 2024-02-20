from rest_framework import serializers
from .models import Doctor, Patient, Prescription, Medication


class BaseDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name')


class BasePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name')


class BaseMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('id', 'name')


class DoctorSerializer(BaseDoctorSerializer):
    class Meta(BaseDoctorSerializer.Meta):
        fields = BaseDoctorSerializer.Meta.fields + ("specialization",)


class PatientSerializer(BasePatientSerializer):
    class Meta(BasePatientSerializer.Meta):
        fields = BasePatientSerializer.Meta.fields + ("date_of_birth", )


class MedicationSerializer(BaseMedicationSerializer):
    class Meta(BaseMedicationSerializer.Meta):
        fields = BaseMedicationSerializer.Meta.fields + ("dosage",)


class PrescriptionGetSerializer(serializers.ModelSerializer):
    doctor = BaseDoctorSerializer()
    patient = BasePatientSerializer()
    medications = BaseMedicationSerializer(many=True)
    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date_prescribed', 'medications']


class PrescriptionSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    medications = serializers.PrimaryKeyRelatedField(many=True, queryset=Medication.objects.all())

    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'date_prescribed', 'medications']