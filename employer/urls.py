from django.urls import path

from .views import (
    EmployerDetailView, EmployerUpdateView
)

urlpatterns = [
    path('<int:id>', EmployerDetailView.as_view(), name='employer_profile'),
    path('<int:id>/edit', EmployerUpdateView.as_view(), name='employer_edit_profile'),
]