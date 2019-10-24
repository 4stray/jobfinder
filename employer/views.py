from django.views.generic import DetailView

from .models import Employer


class EmployerDetailView(DetailView):
    model = Employer
    pk_url_kwarg = 'id'
    context_object_name = 'employer'
