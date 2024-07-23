from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/user/', include('user.urls'), name='user'),
    path('api/announcement/', include('announcement.urls'), name='announcement'),
    path('api/search-announcement/', include('search_announcement.urls'), name='search-announcement'),
    path('api/shelter/', include('shelter.urls'), name='shelter'),
    path('api/shelter-announcement/', include('shelter_announcement.urls'), name='shelter-announcement'),
    path('api/user-feedback/', include('rating.urls'), name='rating'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
