from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ShelterAnnouncementCreateEditViewSet.as_view({'post': 'create'})),
    path('edit/<int:pk>/', views.ShelterAnnouncementCreateEditViewSet.as_view({'put': 'update'})),
    path('detail/<int:pk>/', views.ShelterAnnouncementDetailView.as_view()),
    path('delete/<int:pk>/', views.ShelterAnnouncementDeleteView.as_view()),
    path('list/<int:pk>/', views.ShelterListAnnouncementsView.as_view()),
]