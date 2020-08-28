from django.urls import path, include

from . import views

appname = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
]