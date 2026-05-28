from django import forms
from myapp.models import Employee

class EmployeeForm(forms.ModelForm):
    EmployeeID = forms.IntegerField()
    EmployeeName = forms.CharField(max_length=30)
    EmployeeSalary = forms.DecimalField(max_digits=7,decimal_places=2)
    class Meta:
        model = Employee
        fields = '__all__'