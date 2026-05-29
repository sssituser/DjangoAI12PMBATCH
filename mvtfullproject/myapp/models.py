from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeId = models.IntegerField()
    EmployeeName = models.CharField(max_length=50)
    EmployeeSalary = models.DecimalField(max_digits=7,decimal_places=2)