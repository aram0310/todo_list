from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('create/', views.create, name='create'),
    path('details/<int:pk>', views.todo_details, name='details'),
    path('delete/<int:pk>', views.delete, name='delete'),
]