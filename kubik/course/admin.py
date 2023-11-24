from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect        
from django.conf.urls import url
from django.http.request import HttpRequest
from django.urls import path

from course.models import Course, TimeTable, Application, Enrollment, StudentCourse
from user.models import User
from typing import Any, Union
from django.shortcuts import get_object_or_404


def enrollment(obj):
    context = {'student':obj.student, 'course':obj.course}
    current_course_count = obj.course.enrollers
    current_course_max = obj.course.capacity
    if current_course_count < current_course_max:
        Enrollment.objects.create(**context)
        obj.approved = 1
        obj.save()
        obj.course.save()
    #   ниже вариант с удалением экземпляра заявки на курс
    #   Application.objects.filter(id=obj.id).delete()

@admin.action(description="Зачислить выбранных участников")
def apply(modeladmin, request, queryset):
    for obj in queryset:
        enrollment(obj)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    change_form_template = 'admin/course/change_form_application.html'
    list_display = ['student', 'course', 'approved']
    readonly_fields = ['approved']
    actions = [apply]

    def get_enroll_status(self):
        pass

    def changeform_view(self, request: HttpRequest, object_id: str = ..., form_url: str = ..., extra_context: dict[str, bool] = ...) -> Any:
        extra_context = extra_context or {}
        try:
            application = Application.objects.get(id=object_id)
            if Enrollment.objects.filter(course=application.course, student=application.student):
                extra_context['enrolled'] = True
        except:
            pass
        
        return super().changeform_view(request, object_id, form_url, extra_context=extra_context)

    def response_change(self, request, obj):
        if "apply" in request.POST:
            enrollment(obj)
            return HttpResponseRedirect("../")
        return super().response_change(request, obj)
    

class MembershipInline(admin.TabularInline):
    model = Course.timetable.through
    list_display=['weekday', 'time']

class TimeTableAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    
class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 0

@admin.register(Course)
class CourceAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline, EnrollmentInline
    ]
    exclude = ('timetable',)
    fields  = ['title', 'description', 'teacher', 'capacity', 'enrollers']
