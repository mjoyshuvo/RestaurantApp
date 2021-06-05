from rest_framework import serializers
from apps.restaurant.models import Restaurant, Menu
from conf.permissions import ApiBasePermission
from conf.pagination import LargeResultsSetPagination
from conf.viewset import CustomViewSetForQuerySet


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantViewSet(CustomViewSetForQuerySet):
    serializer_class = RestaurantSerializer
    pagination_class = LargeResultsSetPagination
    model = Restaurant
    permission_classes = [ApiBasePermission]
    permission_id = [1, ]
    queryset = Restaurant.objects.all()


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuViewSet(CustomViewSetForQuerySet):
    serializer_class = MenuSerializer
    pagination_class = LargeResultsSetPagination
    model = Menu
    permission_classes = [ApiBasePermission]
    permission_id = [1, ]
    queryset = Menu.objects.all()
