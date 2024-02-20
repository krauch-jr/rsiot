from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_prescribed = models.DateField(auto_now_add=True)
    medications = models.ManyToManyField('Medication')

    def __str__(self):
        return f"Prescription for {self.patient.name} by {self.doctor.name}"


class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return self.name
