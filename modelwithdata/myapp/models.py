from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeID = models.IntegerField()
    EmployeeName = models.CharField(max_length=50)
    EmployeeSalary = models.IntegerField()
