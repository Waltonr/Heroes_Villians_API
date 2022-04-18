from django.urls import path
from . import views

urlpatterns = [
    path('types/', views.super_types_list)
]