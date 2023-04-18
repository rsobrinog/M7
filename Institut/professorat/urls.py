from django.urls import path
from . import views

urlpatterns = [
    path('llista', views.teachers_list, name='teachers_list'),
]