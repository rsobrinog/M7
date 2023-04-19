from django.urls import path
from . import views

urlpatterns = [
    path('llista', views.teachers_list, name='teachers_list'),
    path('teacher-form/', views.teach_form, name='teach_form'),
    path('update/<str:pk>/', views.update, name='update'),
]