from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename =  models.CharField(max_length=40)
    esal  = models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return self.ename