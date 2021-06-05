from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.restaurant.views import RestaurantViewSet, MenuViewSet, VoteViewSet, make_vote

app_name = 'restaurant'

router = DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menus')
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'vote', VoteViewSet, basename='vote')
router.register(r'vote', VoteViewSet, basename='vote')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^make_vote', make_vote, name='make_vote'),
]
