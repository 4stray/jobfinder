from django.urls import path

from .views import (
    EmployerDetailView, EmployerUpdateView,
    VacancyCreateView, VacancyUpdateView, VacancyDeleteView
)

urlpatterns = [
    path('<int:id>', EmployerDetailView.as_view(), name='employer_profile'),
    path('<int:id>/edit', EmployerUpdateView.as_view(), name='employer_edit_profile'),
    path('<int:employer_id>/vacancies/new', VacancyCreateView.as_view(), name='vacancy_create'),
    path('<int:employer_id>/vacancies/<int:vacancy_id>/edit', VacancyUpdateView.as_view(), name='vacancy_edit'),
    path('<int:employer_id>/vacancies/<int:vacancy_id>/delete', VacancyDeleteView.as_view(), name='vacancy_delete'),
]