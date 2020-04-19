from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EMPTYPE = [
    ('FullTime', 'FullTime'),
    ('PartTime', 'PartTime'),
    ('Internship', 'Internship')
]

class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    emp_type = models.CharField(max_length=50, choices=EMPTYPE, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    cv = models.ImageField(upload_to='emp-docs/cv/', blank=True, null=True)
    idproof = models.ImageField(upload_to='emp-docs/idproof/', blank=True, null=True)
    bankpassbook = models.ImageField(upload_to='emp-docs/bankpassbook/', blank=True, null=True)

    def __str__(self):
        return self.employee.username

    class Meta:
        verbose_name_plural = "Employees"

    def date_good(self):
        return self.dob.strftime('%b %e %Y')