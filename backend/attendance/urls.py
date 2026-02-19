from django.urls import path

from .views import AttendanceListCreateView, DashboardSummaryView

urlpatterns = [
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('dashboard/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]
