from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms

from employee.models import Employee
from employer.models import Employer

ACCOUNT_TYPES = {
    ('eyee', 'Employee'),
    ('eyer', 'Employer'),
}


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required', required=True)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPES, required=True)

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            if self.cleaned_data['account_type'] == 'eyee':
                user.employee = Employee.objects.create()
            elif self.cleaned_data['account_type'] == 'eyer':
                user.employer = Employer.objects.create()
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'account_type')
