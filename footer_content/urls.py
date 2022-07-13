from django.urls import path
from . import views


urlpatterns = [
    path('returns/', views.ReturnsContent, name='returns'),
    path('postage/', views.PostageContent, name='postage'),
    path('privacy/', views.PrivacyContent, name='privacy'),
    path('about/', views.AboutContent, name='about'),
]
