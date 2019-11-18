from django.db import models
from django.urls import reverse
from django.core.validators import (
    URLValidator,
)


from utils.validators import phone_validator


class Employer(models.Model):
    name = models.CharField(max_length=255, blank=False)
    second_name = models.CharField(max_length=255, blank=False)
    company_name = models.CharField(max_length=255, blank=True)
    company_description = models.TextField()
    site_link = models.CharField(max_length=255, blank=True,
                                 validators=[URLValidator()])
    contact_phone = models.CharField(max_length=64, blank=True,
                                     validators=[phone_validator])
    contact_email = models.EmailField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('employer_profile', args=[self.pk])

    @property
    def full_name(self):
        return f'{self.name} {self.second_name}'

    def __str__(self):
        return f'{self.full_name} from {self.company_name}'
