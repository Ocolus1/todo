from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('update/<str:id>/', update, name="update"),
    path('delete/<str:id>/', delete_task, name="delete"),
]