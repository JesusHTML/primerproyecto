from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal2, name='principal2')
]