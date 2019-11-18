from django.urls import path


from .views import (
    EmployeeDetailView, EmployeeUpdateView
)


urlpatterns = [
    path('<int:id>', EmployeeDetailView.as_view(), name='employee_profile'),
    path('<int:id>/edit', EmployeeUpdateView.as_view(), name='employee_edit_profile'),
]