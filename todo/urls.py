from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^todo/$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>[0-9]+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<pk>[0-9]+)/delete/$', views.todo_delete, name='todo_delete')
]