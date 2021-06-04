from django.conf.urls import include
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'Api'

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token, name='api_token'),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    path('', include('apps.user.urls', namespace='users_api'))
]
