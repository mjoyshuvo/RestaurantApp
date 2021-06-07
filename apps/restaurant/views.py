from django.db import transaction
from rest_framework import serializers
from apps.restaurant.models import Restaurant, Menu, Result
from conf.permissions import ApiBasePermission
from conf.pagination import LargeResultsSetPagination
from conf.viewset import CustomViewSetForQuerySet
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from datetime import datetime


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
        extra_kwargs = {'vote_count': {'read_only': True}}


class MenuViewSet(CustomViewSetForQuerySet):
    serializer_class = MenuSerializer
    pagination_class = LargeResultsSetPagination
    model = Menu
    permission_classes = [ApiBasePermission]
    permission_id = [3, ]
    queryset = Menu.objects.all()

    def get_queryset(self):
        current_day = self.request.query_params.get('current_day')
        if current_day:
            queryset = Menu.objects.filter(created_at=datetime.now().date())
            return queryset
        queryset = Menu.objects.all()
        return queryset


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def make_vote(request):
    user = request.user
    current_date = datetime.now().date()
    if user.employee_type == 'Employee':
        menu_id = request.GET['menu_id'] if 'menu_id' in request.GET else None
        if not menu_id:
            raise serializers.ValidationError({"status": 400, "message": "User must provide a menu id"})
        if user.last_vote_date == current_date:
            raise serializers.ValidationError({"status": 400, "message": "You've already cast your vote today"})
        try:
            menu = Menu.objects.get(id=menu_id, created_at=datetime.now().date())
            with transaction.atomic():
                menu.vote_count += 1
                menu.save()
                user.last_vote_date = current_date
                user.save()
                return Response({"status": 200, "message": "You've voted successfully"})
        except Menu.DoesNotExist:
            raise serializers.ValidationError({"status": 400, "message": "Not a valid menu"})
    return Response({"status": 200, "message": "You have to be an employee to vote."})


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def generate_result(request):
    top_menus = Menu.objects.filter(created_at=datetime.now().date()).order_by('-vote_count')[:4]
    previous_results = Result.objects.values_list('restaurant_id', flat=True)[:3]
    for menu in top_menus:
        if menu.restaurant_id not in previous_results:
            Result.objects.create(menu=menu, restaurant=menu.restaurant)
            return Response({"status": 200, "message": "The winner restaurant is {}".format(menu.restaurant.name)})
    return Response({"status": 200, "message": "No result found"})
