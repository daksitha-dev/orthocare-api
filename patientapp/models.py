from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    history = models.TextField()
    future_treatments = models.TextField()

    def __str__(self):
        return f"{self.patient_id} - {self.name}"

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_histories')
    visit_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f'{self.patient.patient_id} - {self.patient.name} (Visit: {self.visit_date})'

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_plan = models.TextField()
    scheduled_date = models.DateField()

    def __str__(self):
        return f'{self.patient.patient_id} - {self.patient.name} (Treatment Date: {self.scheduled_date})'