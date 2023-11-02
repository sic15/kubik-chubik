from django.db import models

from user.models import User

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

    def __str__(self):
        return f'Начало в {self.time} в {self.weekday}'

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='teacher', verbose_name='Преподаватель')
    timetable = models.ManyToManyField(TimeTable, related_name='timetable', verbose_name='Расписание')
    students = models.ManyToManyField(User, blank=True, related_name='students', verbose_name='Ученики')

    def __str__(self):
        return f'Курс {self.title}'


