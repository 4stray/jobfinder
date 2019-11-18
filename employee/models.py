from django.db import models
from django.urls import reverse

from utils.validators import phone_validator


class Employee(models.Model):

    POSITIONS = (
        ('PM', 'Project Manager'),
        ('SE', 'Software Developer/Engineer'),
        ('DevOps', 'DevOps'),
        ('QA', 'Quality Assurance'),
        ('SA', 'System Administrator'),
        ('UI', 'User Interface Designer'),
        ('UX', 'User Experience Designer'),
        ('BA', 'Business Analytic'),
        ('Arch', 'Architect'),
    )

    ENGLISH_LEVELS = (
        ('A1', 'Elementary'),
        ('A2', 'Pre-Intermediate'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper-Intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficient')
    )

    name = models.CharField(max_length=255, blank=False)
    second_name = models.CharField(max_length=255, blank=False)
    self_description = models.TextField(blank=True)
    wanted_position = models.CharField(max_length=255, choices=POSITIONS, blank=True)
    english_level = models.CharField(max_length=255, choices=ENGLISH_LEVELS, default=ENGLISH_LEVELS[0][1])
    work_experience = models.PositiveIntegerField(default=0)

    # Contact
    contact_phone = models.CharField(max_length=64, blank=True,
                                     validators=[phone_validator])
    contact_email = models.EmailField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('employee_profile', args=[self.pk])

    @property
    def full_name(self):
        return f'{self.name} {self.second_name}'

    def __str__(self):
        return f'{self.full_name} lfw as {self.wanted_position}'
