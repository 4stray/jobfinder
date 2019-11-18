from django.contrib.auth.views import LogoutView, LoginView


class UserLoginView(LoginView):
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass
