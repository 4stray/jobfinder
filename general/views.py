from django.views.generic import TemplateView

from employee.models import Employee
from employer.models import Employer
from utils.pagination import get_paginated


class HomePage(TemplateView):
    template_name = 'general/homepage.html'

    def get_context_data(self, **kwargs):
        context_ = super().get_context_data(**kwargs)
        context_['employees'] = get_paginated(self.request, Employee, page_query='page_empe')
        context_['employers'] = get_paginated(self.request, Employer, page_query='page_empr')
        return context_
