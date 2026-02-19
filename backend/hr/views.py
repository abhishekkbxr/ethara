from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from attendance.serializers import AttendanceSerializer
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        employee = self.get_object()
        employee_name = employee.full_name
        self.perform_destroy(employee)
        return Response(
            {'message': f'Employee {employee_name} deleted successfully.'},
            status=status.HTTP_200_OK,
        )


class EmployeeAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_employee(self):
        return get_object_or_404(Employee, pk=self.kwargs['pk'])

    def get_queryset(self):
        return self.get_employee().attendances.select_related('employee').all()
