from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
