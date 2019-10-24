from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)
    second_name = models.CharField(max_length=45, blank=False, null=False)
    company_name = models.CharField(max_length=140, blank=True, null=False)
    company_description = models.TextField()
    site_link = models.CharField(max_length=255, blank=True, null=False)
    contact_phone = models.CharField(max_length=12, blank=True, null=False)
    contact_email = models.EmailField(max_length=32, blank=True, null=False)

    @property
    def full_name(self):
        return f'{self.name} {self.second_name}'

    def __str__(self):
        return f'{self.full_name} from {self.company_name}'
