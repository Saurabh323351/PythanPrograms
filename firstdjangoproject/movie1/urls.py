from django.conf.urls import url

from django.urls import path
from  . import views

urlpatterns = [
    url(r'^$', views.index),
    path('tp1' , views.letsee),
    path('company_name',views.company_details),
]

