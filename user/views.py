from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView
from django.urls import reverse

from .forms import RegistrationForm


class UserLoginView(LoginView):
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


class UserRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def get_success_url(self):
        return reverse('homepage')
