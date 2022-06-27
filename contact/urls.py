from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactPage, name='contact'),
]