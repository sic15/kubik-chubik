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

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='course_teacher')
    timetable = models.ManyToManyField(TimeTable)
    students = models.ManyToManyField(User)

    def __str__(self):
        return f'Курс {self.title}'


