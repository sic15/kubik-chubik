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
    middle_name = models.CharField(max_length=20, verbose_name='отчество')
    last_name = models.CharField(
        max_length=30,
        verbose_name='фамилия'
    )
    type = models.CharField(max_length=20, choices=UserTipes)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class TimeTable(models.Model):
    week = [('Monday', 'Понедельник'),
            ('Tuesday', 'Вторник'),
            ('Wednesday', 'Среда'),
            ('Thursday', 'Четверг'),
            ('Friday', 'Пятница'),
            ('Saturday', 'Суббота'),
            ('Sunday', 'Воскресенье')]
    weekday = models.CharField(max_length=10,
                               choices=week, verbose_name='день недели')
    time = models.TimeField(verbose_name='время начала')
    duration = models.IntegerField(verbose_name='продолжительность')

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='course_teacher')
    timetable = models.ManyToManyField(TimeTable)
    students = models.ManyToManyField(User)

    def __str__(self):
        return f'Курс {self.title}'


