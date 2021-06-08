from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.restaurant.views import RestaurantViewSet, MenuViewSet, ResultViewSet, make_vote, generate_result

app_name = 'restaurant'

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'results', ResultViewSet, basename='results')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^make_vote', make_vote, name='make_vote'),
    url(r'^generate_result', generate_result, name='generate_result')
]
