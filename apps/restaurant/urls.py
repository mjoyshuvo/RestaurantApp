from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.restaurant.views import RestaurantViewSet, MenuViewSet

app_name = 'restaurant'

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')

urlpatterns = [
    path('', include(router.urls))
]
