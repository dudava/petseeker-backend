from django.urls import path, include

from . import views

urlpatterns = [
    path('load/profile/', views.ProfileImageLoadView.as_view()),
    path('load/shelter/<int:pk>/', views.ShelterImageLoadView.as_view()),
]
