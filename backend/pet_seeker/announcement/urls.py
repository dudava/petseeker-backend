from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('create/', views.PrivateAnnouncementCreateEditViewSet.as_view({'post': 'create'})),
    path('edit/<int:pk>/', views.PrivateAnnouncementCreateEditViewSet.as_view({'put': 'update'})),
    path('detail/<int:pk>/', views.PrivateAnnouncementDetailView.as_view()),
    path('delete/<int:pk>/', views.PrivateAnnouncementDeleteView.as_view()),
]
