from django.db import models

from user.models import User


class TimeTable(models.Model):
    WEEKDAYS = (('Monday', 'Понедельник'),
               ('Tuesday', 'Вторник'),
               ('Wednesday', 'Среда'),
               ('Thursday', 'Четверг'),
               ('Friday', 'Пятница'),
               ('Saturday', 'Суббота'),
               ('Sunday', 'Воскресенье'))
    weekday = models.CharField(max_length=10,
                               choices=WEEKDAYS, verbose_name='день недели')
    time = models.TimeField(verbose_name='время начала')
    duration = models.SmallIntegerField(verbose_name='продолжительность')

    def __str__(self):
        return f'Начало в {self.time} в {self.weekday}'
    
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses', verbose_name='Преподаватель')
    timetable = models.ManyToManyField(TimeTable, related_name='courses', verbose_name='Расписание')
    capacity = models.PositiveSmallIntegerField(verbose_name='Максимальное число учеников', default=10)
    enrollers = models.PositiveSmallIntegerField(verbose_name='Количество учеников в группе', default=0)

    def __str__(self):
        return f'Курс {self.title}'
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class StudentCourse(models.Model):
    student = models.ForeignKey(User, related_name='%(class)s', on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, related_name='%(class)s', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self) -> str:
        return f'{self.student} - {self.course}'

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_%(class)s_entry'
            )
        ]


class Application(StudentCourse):
    approved = models.BooleanField('Подтверждение', default=False)
    
    class Meta(StudentCourse.Meta):
        verbose_name = 'Заявка на курс'
        verbose_name_plural = 'Заявки на курс'


class Enrollment(StudentCourse):
    
    class Meta(StudentCourse.Meta):
        verbose_name = 'Участник курса'
        verbose_name_plural = 'Участники курса'
