import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )
    if re.search(r'^[a-zA-Z][z-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            (f'Недопустимые символы <{value}> в имени.'),
            params={'value': value},
        )


def validate_year(value):
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            f'Указанный год - {value} не может быть больше {now}',
            params={'value': value}
        )