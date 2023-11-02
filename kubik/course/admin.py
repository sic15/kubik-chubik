from django.contrib import admin

from .models import Course, TimeTable


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
    

@admin.register(Course)
class CourceAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('timetable',)
