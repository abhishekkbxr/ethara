from django.db.models import Count, Q
from rest_framework import generics
from rest_framework.response import Response

from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.select_related('employee').all()
        employee_id = self.request.query_params.get('employee_id')
        date = self.request.query_params.get('date')

        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        if date:
            queryset = queryset.filter(date=date)

        return queryset


class DashboardSummaryView(generics.GenericAPIView):
    def get(self, request):
        summary = Attendance.objects.aggregate(
            total_records=Count('id'),
            total_present=Count('id', filter=Q(status='Present')),
            total_absent=Count('id', filter=Q(status='Absent')),
        )
        return Response(summary)
