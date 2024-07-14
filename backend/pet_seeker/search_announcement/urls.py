from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementSearchViewSet.as_view({'get': 'list'})),
]
