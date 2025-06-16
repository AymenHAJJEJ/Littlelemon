from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

# DRF router for API endpoints
router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='bookings')

# HTML page routes (non-API)
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name='bookings'),  # custom JSON booking handler
]

# DRF API endpoints (/api/bookings/) exposed in project urls.py
api_urlpatterns = router.urls