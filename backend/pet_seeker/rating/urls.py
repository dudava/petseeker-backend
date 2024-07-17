from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserFeedbackCreateEditViewSet.as_view({'post': 'create'})),
]