from django.db import models
from django.urls import reverse
from django.core.validators import (
    URLValidator,
)


from .validators import phone_validator


class Employer(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)
    second_name = models.CharField(max_length=45, blank=False, null=False)
    company_name = models.CharField(max_length=140, blank=True, null=False)
    company_description = models.TextField()
    site_link = models.CharField(max_length=255, blank=True, null=False,
                                 validators=[URLValidator()])
    contact_phone = models.CharField(max_length=12, blank=True, null=False,
                                     validators=[phone_validator])
    contact_email = models.EmailField(max_length=32, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('employer_profile', args=[self.pk])

    @property
    def full_name(self):
        return f'{self.name} {self.second_name}'

    def __str__(self):
        return f'{self.full_name} from {self.company_name}'
