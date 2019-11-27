from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse

from .models import Employer, Vacancy


class EmployerDetailView(DetailView):
    model = Employer
    pk_url_kwarg = 'id'
    context_object_name = 'employer'


class EmployerUpdateView(UpdateView):
    model = Employer
    fields = '__all__'
    pk_url_kwarg = 'id'
    template_name_suffix = '_update'


class VacancyCreateView(CreateView):
    model = Vacancy
    fields = '__all__'
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse('employer_profile', args=[self.kwargs.get('employer_id')])
