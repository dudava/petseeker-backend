from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register('user', views.UserViewSet)
router.register('user_info', views.UserInfoViewSet)

urlpatterns = [
    path('register', views.UserRegisterAPIView.as_view()),
    path('detail/<int:pk>/', views.UserDetail.as_view()),
    path('me/', views.UserMeView.as_view()),
    path('', include(router.urls)),
]
