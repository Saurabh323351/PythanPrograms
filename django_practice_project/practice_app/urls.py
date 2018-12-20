

from django.urls import path
from  . import views

urlpatterns = [

    path('' , views.try_it),
    path('time',views.get_system_time),
    path('info',views.employee_info_view),
    path('database_record',views.get_or_create_db_record),
    path('student_form',views.student_form),
    path('message',views.success)
]

