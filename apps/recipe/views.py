from rest_framework import viewsets
from .models import Doctor, Patient, Prescription, Medication
from .seriializers import DoctorSerializer, PatientSerializer, MedicationSerializer, PrescriptionSerializer, \
    PrescriptionGetSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PrescriptionGetSerializer
        return PrescriptionSerializer
