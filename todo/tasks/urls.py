from django.conf.urls import url 
from . import views

urlpatterns = [
    url('^$', views.index, name='list'),
    url('(?P<pk>\d+)/$', views.updateTask, name="update_task"),
    url('(?P<pk1>\d+)/delete/', views.deleteTask, name="delete"),
]
