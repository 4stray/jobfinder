from django.urls import path

from .views import EmployerDetailView

urlpatterns = [
    path('<int:id>', EmployerDetailView.as_view(), name='employer_profile')
]