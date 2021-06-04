import operator
from functools import reduce

from django.db.models import Q
from rest_framework import viewsets


class CustomViewSetForQuerySet(viewsets.ModelViewSet):
    model = None
    change_keys = None
    search_keywords = None
    permission_id = None

    def get_permissions(self):
        if self.permission_id is None:
            raise AssertionError(
                'CustomViewSetForQuerySet need to include a permission_id')

        for permission in self.permission_classes:
            if permission.__name__ == 'ApiBasePermission':
                return [permission(self.permission_id)]
            else:
                return [permission()]
