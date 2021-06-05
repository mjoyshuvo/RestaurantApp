from django.urls import path
from django.conf.urls import include
from apps.api.views import LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'Api'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('', include('apps.user.urls', namespace='users_api')),
    path('', include('apps.restaurant.urls', namespace='restaurant_api'))
]
