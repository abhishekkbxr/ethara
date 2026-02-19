from django.db import IntegrityError
from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email', 'department', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'employee_id': {
                'error_messages': {'unique': 'Employee ID already exists.'},
            },
            'email': {
                'error_messages': {
                    'invalid': 'Enter a valid email address.',
                    'unique': 'Email already exists.',
                }
            },
        }

    def validate_employee_id(self, value):
        if not value.strip():
            raise serializers.ValidationError('Employee ID cannot be blank.')
        return value.strip()

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Full name cannot be blank.')
        return value.strip()

    def validate_department(self, value):
        if not value.strip():
            raise serializers.ValidationError('Department cannot be blank.')
        return value.strip()

    def validate_email(self, value):
        return value.strip().lower()

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            msg = str(exc).lower()
            if 'employee_id' in msg:
                raise serializers.ValidationError(
                    {'employee_id': 'Employee ID already exists.'}
                ) from exc
            if 'email' in msg:
                raise serializers.ValidationError({'email': 'Email already exists.'}) from exc
            raise serializers.ValidationError(
                {'employee_id': 'Duplicate employee record detected.'}
            ) from exc
