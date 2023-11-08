from django.contrib import admin
from django import forms

from .models import Course, TimeTable
from user.models import User


#admin.site.register(Course)
admin.site.register(TimeTable)

"""
class ItemInline(admin.StackedInline):
    model = TimeTable
 #   extra = 5

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
   # exclude = ('Timetable',)
   # list_display = ["created", "total_price", "paid"]

   """


class MembershipInline(admin.TabularInline):
    model = Course.timetable.through
    list_display=['weekday', 'time']



class TimeTableAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    
class CourseForm(forms.BaseModelForm):
    
    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher', 'students']



@admin.register(Course)
class CourceAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    form = CourseForm()
  #  exclude=['timetable']
   # fields = ['title', 'description', 'teacher', 'students']
    

