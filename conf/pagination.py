from rest_framework.pagination import LimitOffsetPagination
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from collections import OrderedDict


class LargeResultsSetPagination(LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = 'start'
    max_limit = 100

    def get_paginated_response(self, data):
        try:
            draw = self.request.query_params.get('draw')
        except MultiValueDictKeyError:
            draw = 1

        return Response(OrderedDict([
            ('recordsTotal', self.count),
            ('recordsFiltered', self.count),
            ('draw', draw),
            ('data', data)
        ]))