from django.contrib import admin

from course.models import Course, TimeTable, Application, Enrollment


admin.site.register(Course)
admin.site.register(TimeTable)
admin.site.register(Enrollment)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass

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


# class MembershipInline(admin.TabularInline):
#     model = Course.timetable.through
#     list_display=['weekday', 'time']

# class TimeTableAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
    

# @admin.register(Course)
# class CourceAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('timetable',)
