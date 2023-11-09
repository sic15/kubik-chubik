from django.contrib import admin

from .models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name',
              'middle_name', 'last_name', 'type', 'password']
    list_display = ['first_name', 'last_name', 'type']

