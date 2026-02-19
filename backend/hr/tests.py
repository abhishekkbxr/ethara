from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EmployeeApiTests(APITestCase):
    def test_create_employee_success(self):
        payload = {
            'employee_id': 'EMP-001',
            'full_name': 'Ava Johnson',
            'email': 'ava@company.com',
            'department': 'Engineering',
        }

        response = self.client.post(reverse('employee-list-create'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['employee_id'], payload['employee_id'])

    def test_duplicate_employee_id_returns_400(self):
        payload = {
            'employee_id': 'EMP-001',
            'full_name': 'Ava Johnson',
            'email': 'ava@company.com',
            'department': 'Engineering',
        }
        self.client.post(reverse('employee-list-create'), payload, format='json')

        duplicate_payload = {
            'employee_id': 'EMP-001',
            'full_name': 'Mila Carter',
            'email': 'mila@company.com',
            'department': 'HR',
        }
        response = self.client.post(
            reverse('employee-list-create'), duplicate_payload, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)
