from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect        
from django.conf.urls import url
from django.http.request import HttpRequest
from django.urls import path

from course.models import Course, TimeTable, Application, Enrollment
from user.models import User
from typing import Any, Union
from django.shortcuts import get_object_or_404


#admin.site.register(Course)
#admin.site.register(TimeTable)
#admin.site.register(Enrollment)

def enrollment(obj):
    context = {'student':obj.student, 'course':obj.course}
    current_course_count = obj.course.enrollers
    current_course_max = obj.course.capacity
    if current_course_count < current_course_max:
        Enrollment.objects.create(**context)
      #  new_course_count = obj.course.enrollers
      #  if new_course_count > current_course_count:
        obj.approved = 1
        obj.save()
          #  current_course.enrollers += 1
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
    
    
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    pass

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass
"""
    def save_model(self, request, obj, form, change):
        print('метод save в админке')
        obj.course.enrollers += 1
        obj.course.save()
        obj.save()

    def delete_queryset(self, request, queryset):
        print('метод delete в админке')
        for obj in queryset:
            print('удалили студента')
            obj.course.enrollers -= 1
            obj.course.save()
        queryset.delete()
"""

"""

    def get_urls(self):
	# метод обработки url, с подстановкой необходимой view.

        urls = super(Application, self).get_urls()
        custom_urls = [
            path('get/', self.admin_site.admin_view(self.get_repayment), name='repayment_view'), ]
        return  custom_urls + urls

    def get_repayment(self, request):
    	# внутри данного метода (который подставится под запрос url), мы выполним какую-либо логику, и вернем в ответ пользовательский шаблон index.html
        return render(request, 'index.html', locals())

    # переопределяем атрибут для принудительного использования нашего шаблона:
    """
    
"""
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    change_list_template = "path/to/change_form.html"



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
