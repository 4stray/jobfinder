from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail

from employer.models import Employer
from employee.models import Employee

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    last_login = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    employer = models.OneToOneField(Employer, null=True,
                                    blank=True, on_delete=models.SET_NULL)
    employee = models.OneToOneField(Employee, null=True,
                                    blank=True, on_delete=models.SET_NULL)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.get_short_name()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.email.split('@')[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        return self.is_superuser
