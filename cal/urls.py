from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:id>',views.submit,name='submit'),
]
