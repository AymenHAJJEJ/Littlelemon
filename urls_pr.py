from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import DRF routers and viewsets
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

# Set up DRF router
router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('api/', include(router.urls)),  # Now includes /api/bookings/
    path('api/', include('djoser.urls')),  # User registration etc.
    path('api/auth/', include('djoser.urls.authtoken')),  # Login/logout with tokens
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
