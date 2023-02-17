from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USER_ROLES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ'),
    )

    email = models.EmailField(
        'Адрес почты',
        blank=False,
        unique=True,
        max_length=320,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True
    )
    role = models.CharField(
        'Роль',
        max_length=16,
        choices=USER_ROLES,
        default=USER,
    )
    code = models.CharField(
        'Код подтверждения',
        max_length=100,
        blank=True,
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.is_superuser or self.role == self.ADMIN

    def __str__(self):
        return self.username
