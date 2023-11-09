from django.contrib import admin
from django.http import HttpResponseRedirect        
from django.conf.urls import url
from django.urls import path

from course.models import Course, TimeTable, Application, Enrollment


#admin.site.register(Course)
#admin.site.register(TimeTable)
#admin.site.register(Enrollment)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    change_form_template = 'admin/course/change_form.html'

    def response_change(self, request, obj):
        if "applicate" in request.POST:
            context = {'student':obj.student, 'course':obj.course}
            Enrollment.objects.get_or_create(**context)
            Application.objects.filter(id=obj.id).delete()
         #   obj.approved = 1
        #    print(obj.__dict__)
            return HttpResponseRedirect("../")
        return super().response_change(request, obj)

 #   def get_urls(self):
 #       urls = super().get_urls()
 ##       print('11111111111')
  #      return urls
  #  pass

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'
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
    



 #   change_list_template = "admin/change_list1.html"
"""
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    change_list_template = "path/to/change_form.html"

    def get_urls(self):
        urls = super(EnrollmentAdmin, self).get_urls()
        print('11111111111111111111')
        custom_urls = [
        url('^import/$', self.process_import_btmp, name='process_import'),]
        return custom_urls + urls
    def process_import_btmp(self, request):
       # import_custom = ImportCustom()
        #count = import_custom.import_data()
        self.message_user(request, f"создано 12 новых записей")
        return HttpResponseRedirect("../")


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
