from django.urls import path
from . import views

urlpatterns = [
    path('returns/', views.returns, name='returns'),
    path('postage/', views.postage, name='postage'),
    path('privacy/', views.privacy, name='privacy'),
]