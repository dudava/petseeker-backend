from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementSearchViewSet.as_view(), name='announcement_search'),
    path('private-announcement/', views.PrivateAnnouncementSearchViewSet.as_view(), name='announcement_search'),
    path('shelter-announcement/', views.ShelterAnnouncementSearchViewSet.as_view(), name='announcement_search'),
    path('private-announcement/me', views.MyPrivateAnnouncementSearchViewSet.as_view(), name='announcement_search'),
    path('shelter-announcement/me', views.MyShelterAnnouncementSearchViewSet.as_view(), name='announcement_search')
]