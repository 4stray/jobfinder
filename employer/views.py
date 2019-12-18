from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect

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
    fields = ['title', 'description', 'position']
    template_name_suffix = '_create'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)

            obj.employer_id = kwargs.get('employer_id', None)
            obj.save()
            return redirect(reverse('employer_profile', args=[self.kwargs.get('employer_id')]))


class VacancyDeleteView(DeleteView):
    model = Vacancy
    pk_url_kwarg = 'vacancy_id'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('employer_profile', args=[self.kwargs.get('employer_id')])


class VacancyUpdateView(UpdateView):
    model = Vacancy
    fields = ['title', 'description', 'position', 'is_active']
    pk_url_kwarg = 'vacancy_id'
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('employer_profile', args=[self.kwargs.get('employer_id')])