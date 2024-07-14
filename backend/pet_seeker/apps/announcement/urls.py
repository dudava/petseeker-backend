from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('create/', views.AnnouncementCreateEditViewSet.as_view({'post': 'create'})),
    path('edit/<int:pk>/', views.AnnouncementCreateEditViewSet.as_view({'put': 'update'})),
    path('detail/<int:pk>/', views.AnnouncementDetailView.as_view()),
    path('delete/<int:pk>/', views.AnnouncementDeleteView.as_view()),
]
