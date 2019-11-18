from django.views.generic import DetailView, UpdateView

from .models import Employee


class EmployeeDetailView(DetailView):
    model = Employee
    pk_url_kwarg = 'id'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    pk_url_kwarg = 'id'
    template_name_suffix = '_update'
