from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView
from django.urls import reverse

from . import forms


class UserLoginView(LoginView):
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


class UserRegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = 'registration/registration.html'

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context_ = super().get_context_data(**kwargs)

        context_['employer_form'] = forms.EmployerForm()
        context_['employee_form'] = forms.EmployeeForm()

        return context_
