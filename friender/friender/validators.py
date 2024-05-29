from django.core.exceptions import ValidationError


def users_age_validator(value):
    if int(value) < 18:
        raise ValidationError(
            "Age must be more than 18 "
        )
    elif  int(value) > 90:
        raise ValidationError(
            "Age must be less than 90 "
        )