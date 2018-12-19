from django.contrib import admin
from practice_app.models import Employee
from practice_app.models import Student


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'e_department', 'e_post', 'eid', 'e_address']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'st_name', 'st_rollno', 'st_address', 'st_qualification']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student,StudentAdmin)
