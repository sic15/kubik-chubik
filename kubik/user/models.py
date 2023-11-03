from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):
    UserTipes = [('teacher', 'Преподаватель'),
                 ('admin', 'Администратор'),
                 ('student', 'Ученик'),
                 ('parent', 'Родитель')]
    username = models.CharField(
        max_length=30,
        verbose_name='username',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    email = models.EmailField(
        max_length=40,
        unique=True,
        verbose_name='email',
    )
    first_name = models.CharField(
        max_length=20,
        verbose_name='имя'
    )
    middle_name = models.CharField(max_length=20, verbose_name='отчество', blank=True)
    last_name = models.CharField(
        max_length=30,
        verbose_name='фамилия'
    )
    type = models.CharField(max_length=20, choices=UserTipes, verbose_name='Роль')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

