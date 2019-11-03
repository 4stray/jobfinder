from django.views.generic import DetailView, UpdateView

from .models import Employer


class EmployerDetailView(DetailView):
    model = Employer
    pk_url_kwarg = 'id'
    context_object_name = 'employer'


class EmployerUpdateView(UpdateView):
    model = Employer
    fields = '__all__'
    pk_url_kwarg = 'id'
    template_name_suffix = '_update'
