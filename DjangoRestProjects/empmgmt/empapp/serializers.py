from rest_framework  import serializers
from empapp.models import Employee

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'