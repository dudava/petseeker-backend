from django.urls import path

from . import views

urlpatterns = [
    path('private-announcement/<int:pk>/', views.PrivateAnnouncementFavouriteView.as_view()),
    path('shelter-announcement/<int:pk>/', views.ShelterAnnouncementFavouriteView.as_view()),
    path('', views.GetFavouritesView.as_view()),
]
