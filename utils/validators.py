from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'[0-9]{12}', message='Enter a valid phone number only in digits with length of 12')