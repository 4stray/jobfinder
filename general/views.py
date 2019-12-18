from django.views.generic import TemplateView

from employee.models import Employee
from employer.models import Employer, Vacancy
from utils.pagination import get_paginated


class HomePage(TemplateView):
    template_name = 'general/homepage.html'

    def get_context_data(self, **kwargs):
        context_ = super().get_context_data(**kwargs)

        empe_filter, empr_filter = self.request.GET.get('empe_srch'), self.request.GET.get('empr_srch')
        vac_filter = self.request.GET.get('vac_srch')

        employees = Employee.objects.order_by('user__created', 'name')
        if empe_filter:
            employees = employees.filter(name__icontains=empe_filter)

        employers = Employer.objects.order_by('user__created', 'name')
        if empr_filter:
            employers = employers.filter(name__icontains=empr_filter)

        vacancies = Vacancy.objects.filter(is_active=True).order_by('employer__user__created', 'title')
        if vac_filter:
            vacancies = vacancies.filter(title__icontains=vac_filter)

        context_['employees'] = get_paginated(self.request, employees, page_query='page_empe')
        context_['employers'] = get_paginated(self.request, employers, page_query='page_empr')
        context_['vacancies'] = get_paginated(self.request, vacancies, page_query='page_vac')

        return context_
