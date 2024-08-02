from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/user/', include('user_info.urls'), name='user_info'),
    path('api/sms-verification/', include('sms_verification.urls'), name='sms-verification'),
    path('api/private-announcement/', include('announcement.urls'), name='announcement'),
    path('api/search-announcement/', include('search_announcement.urls'), name='search-announcement'),
    path('api/shelter/', include('shelter.urls'), name='shelter'),
    path('api/shelter-announcement/', include('shelter_announcement.urls'), name='shelter-announcement'),
    path('api/user-feedback/', include('rating.urls'), name='rating'),
    path('api/image-loader/', include('image_loader.urls'), name='image-loader'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
