from django.urls import path
from . import views

#localhost:8000/chai

urlpatterns = [
    path('', views.chai, name="chai"),
]
