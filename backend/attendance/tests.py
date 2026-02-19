from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from hr.models import Employee


class AttendanceApiTests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            employee_id='EMP-001',
            full_name='Ava Johnson',
            email='ava@company.com',
            department='Engineering',
        )

    def test_create_attendance_success(self):
        payload = {
            'employee': self.employee.id,
            'date': str(date.today()),
            'status': 'Present',
        }

        response = self.client.post(reverse('attendance-list-create'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'Present')

    def test_duplicate_attendance_same_day_returns_400(self):
        payload = {
            'employee': self.employee.id,
            'date': str(date.today()),
            'status': 'Absent',
        }
        self.client.post(reverse('attendance-list-create'), payload, format='json')

        response = self.client.post(reverse('attendance-list-create'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)

    def test_filter_attendance_by_employee(self):
        self.client.post(
            reverse('attendance-list-create'),
            {'employee': self.employee.id, 'date': '2026-01-01', 'status': 'Present'},
            format='json',
        )

        response = self.client.get(
            f"{reverse('attendance-list-create')}?employee_id={self.employee.id}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
