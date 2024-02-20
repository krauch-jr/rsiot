# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, PrescriptionViewSet, MedicationViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]