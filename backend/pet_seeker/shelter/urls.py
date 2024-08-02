from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ShelterCreateEditViewSet.as_view({'post': 'create'})),
    path('edit/<int:pk>/', views.ShelterCreateEditViewSet.as_view({'put': 'update'})),
    path('list/', views.ShelterListViewSet.as_view({'get': 'list'})),
    path('user-shelters/<int:pk>/', views.UserSheltersView.as_view()),
    path('detail/<int:pk>/', views.ShelterDetailView.as_view()),
    path('delete/<int:pk>/', views.ShelterDeleteView.as_view()),
]