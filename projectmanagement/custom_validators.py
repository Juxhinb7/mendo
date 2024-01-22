from django.core.validators import ValidationError
import datetime


def validate_date(date):
    if date < datetime.datetime.now():
        raise ValidationError("Date cannot be in the past!")
