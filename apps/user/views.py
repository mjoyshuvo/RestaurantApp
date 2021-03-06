from django.contrib.auth.hashers import make_password
from rest_framework import serializers, viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from apps.user.models import UserProfile
from rest_framework.filters import SearchFilter, OrderingFilter
from conf.permissions import ApiBasePermission
from conf.pagination import LargeResultsSetPagination
from conf.viewset import CustomViewSetForQuerySet


def validate_restaurant(restaurant):
    if not restaurant:
        raise serializers.ValidationError(
            {"status": 400, "message": "Employee type Restaurant must select a Restaurant"})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['user_permissions', 'groups']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password')
        employee_type = validated_data.get('employee_type')
        restaurant = validated_data.get('restaurant')
        if employee_type == 'Restaurant':
            validate_restaurant(restaurant)
        validated_data.update({'password': make_password(password)})
        user = UserProfile.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        employee_type = validated_data.get('employee_type')
        restaurant = validated_data.get('restaurant')
        if employee_type == 'Restaurant':
            validate_restaurant(restaurant)
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UserViewSet(CustomViewSetForQuerySet):
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = UserSerializer
    pagination_class = LargeResultsSetPagination
    model = UserProfile
    permission_classes = [ApiBasePermission]
    permission_id = [1, ]
    queryset = UserProfile.objects.all()
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('first_name', 'last_name')


def jwt_response_payload_handler(token, user=None, request=None):
    #  pass additional data with jwt token
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
