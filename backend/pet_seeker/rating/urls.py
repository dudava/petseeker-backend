from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserFeedbackCreateEditViewSet.as_view({'post': 'create'})),
    path('delete/<int:pk>/', views.UserFeedbackDeleteView.as_view()),
    path('list/<int:pk>/', views.UserFeedbackListView.as_view()),
]
