from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register('user', views.UserViewSet)

urlpatterns = [
    path('signup/', views.UserRegisterView.as_view()),
    path('detail/<int:pk>/', views.UserDetailView.as_view()),
    path('me/', views.UserMeView.as_view()),
    path('user_info/', views.UserInfoEditView.as_view()),
    path('', include(router.urls)),
]
