from django.urls import path

from .views import EmployeeAttendanceView, EmployeeDeleteView, EmployeeListCreateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path(
        'employees/<int:pk>/attendance/',
        EmployeeAttendanceView.as_view(),
        name='employee-attendance',
    ),
]
