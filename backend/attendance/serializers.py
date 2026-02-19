from rest_framework import serializers

from hr.models import Employee
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_code = serializers.CharField(source='employee.employee_id', read_only=True)

    class Meta:
        model = Attendance
        fields = [
            'id',
            'employee',
            'employee_name',
            'employee_code',
            'date',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'employee_name', 'employee_code']

    def validate_employee(self, value):
        if not Employee.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError('Employee not found.')
        return value

    def validate(self, attrs):
        employee = attrs.get('employee')
        date = attrs.get('date')

        if employee and date:
            qs = Attendance.objects.filter(employee=employee, date=date)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    {'date': 'Attendance for this employee and date already exists.'}
                )
        return attrs
