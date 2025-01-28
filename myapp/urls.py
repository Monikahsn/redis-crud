from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('read/<str:key>/', views.read, name='read'),
    path('update/<str:key>/', views.update, name='update'),
    path('delete/<str:key>/', views.delete, name='delete'),
]
