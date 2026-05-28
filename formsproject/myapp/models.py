from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeID = models.IntegerField()
    EmployeeName = models.CharField(max_length=30)
    EmployeeSalary = models.DecimalField(max_digits=7,decimal_places=2)