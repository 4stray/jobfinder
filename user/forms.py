from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms

from uuid import uuid4

from employee.models import Employee
from employer.models import Employer

ACCOUNT_TYPES = {
    ('eyee', 'Employee'),
    ('eyer', 'Employer'),
}


class IdentifiedFormMixin(object):
    _uid = None

    @property
    def uid(self):
        if not self._uid:
            self._uid = uuid4()
        return self._uid


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required', required=True)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPES, required=True)

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            if self.cleaned_data['account_type'] == 'eyee':
                form = EmployeeForm(self.data)
                if form.is_valid():
                    user.employee = form.save()
            elif self.cleaned_data['account_type'] == 'eyer':
                form = EmployerForm(self.data)
                if form.is_valid():
                    user.employer = form.save()
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'account_type')


class EmployeeForm(forms.ModelForm, IdentifiedFormMixin):

    class Meta:
        model = Employee
        fields = ('name', 'second_name', 'wanted_position', 'work_experience')


class EmployerForm(forms.ModelForm, IdentifiedFormMixin):

    class Meta:
        model = Employer
        fields = ('name', 'second_name', 'company_name', 'contact_email')
