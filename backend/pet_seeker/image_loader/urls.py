from django.urls import path, include

from . import views

urlpatterns = [
    path('load/profile/', views.ProfileImageLoadView.as_view()),
    path('load/shelter/<int:pk>/', views.ShelterImageLoadView.as_view()),
    path('load/private-announcement/<int:pk>/', views.PrivateAnnouncementImageLoadView.as_view()),
    path('load/shelter-announcement/<int:pk>/', views.ShelterAnnouncementImageLoadView.as_view()),
    path('delete/profile/', views.ProfileImageDeleteView.as_view()),
    path('delete/shelter/<int:pk>/', views.ShelterImageDeleteView.as_view()),
    path('delete/private-announcement/<int:pk>/', views.PrivateAnnouncementImageDeleteView.as_view()),
    path('delete/shelter-announcement/<int:pk>/', views.ShelterAnnouncementImageDeleteView.as_view()),
]
