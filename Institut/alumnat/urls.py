from django.urls import path
from . import views

urlpatterns = [
    path('llista', views.students_list, name='students_list'),
    path('student-form/', views.stu_form, name='stu_form')
]