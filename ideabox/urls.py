from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ideabox-home'),
    path('about/', views.about, name='ideabox-about')
    
    ]


