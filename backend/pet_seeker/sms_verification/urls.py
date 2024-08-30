from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.SmsVerificationCodeCreateView.as_view()),
    path('auth/', views.SmsAuthView.as_view()),
    path('logout/', views.SmsLogoutView.as_view())
]
