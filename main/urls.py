from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Добавьте другие URL-шаблоны здесь, если они есть
]