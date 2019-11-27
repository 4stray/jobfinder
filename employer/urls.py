from django.urls import path

from .views import (
    EmployerDetailView, EmployerUpdateView,
    VacancyCreateView,
)

urlpatterns = [
    path('<int:id>', EmployerDetailView.as_view(), name='employer_profile'),
    path('<int:id>/edit', EmployerUpdateView.as_view(), name='employer_edit_profile'),
    path('<int:employer_id>/vacancies/new', VacancyCreateView.as_view(), name='vacancy_create')
]