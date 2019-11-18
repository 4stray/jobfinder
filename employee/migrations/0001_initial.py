# Generated by Django 2.2.6 on 2019-11-17 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('self_description', models.TextField(blank=True)),
                ('wanted_position', models.CharField(blank=True, choices=[('PM', 'Project Manager'), ('SE', 'Software Developer/Engineer'), ('DevOps', 'DevOps'), ('QA', 'Quality Assurance'), ('SA', 'System Administrator'), ('UI', 'User Interface Designer'), ('UX', 'User Experience Designer'), ('BA', 'Business Analytic'), ('Arch', 'Architect')], max_length=255)),
                ('english_level', models.CharField(choices=[('A1', 'Elementary'), ('A2', 'Pre-Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper-Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficient')], default='Elementary', max_length=255)),
                ('work_experience', models.PositiveIntegerField(default=0)),
                ('contact_phone', models.CharField(blank=True, max_length=64, validators=[django.core.validators.RegexValidator('[0-9]{12}', message='Enter a valid phone number only in digits with length of 12')])),
                ('contact_email', models.EmailField(blank=True, max_length=255)),
            ],
        ),
    ]