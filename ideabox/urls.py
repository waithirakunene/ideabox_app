from django.urls import path
from .views import (IdeaListView, 
					IdeaDetailView, 
					IdeaCreateView,
					IdeaUpdateView,
					IdeaDeleteView
					)
from . import views

urlpatterns = [
    path('', IdeaListView.as_view(), name='ideabox-home'),
    path('ideas/new', IdeaCreateView.as_view(), name='ideas-create'),
    path('ideas/<int:pk>/', IdeaDetailView.as_view(), name='ideas-detail'),
    path('ideas/<int:pk>/update/', IdeaUpdateView.as_view(), name='ideas-update'),
    path('ideas/<int:pk>/delete/', IdeaDeleteView.as_view(), name='ideas-delete'),
	path('about/', views.about, name='ideabox-about')
    
    ]
