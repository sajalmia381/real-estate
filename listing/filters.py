from django.db.models import Q
from django_filters import rest_framework as filters

from listing.models import Listing


class ListingFilter(filters.FilterSet):
    q = filters.CharFilter(method='custom_method_lookup')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    min_square_feet = filters.NumberFilter(field_name="square_feet", lookup_expr='gte')
    max_square_feet = filters.NumberFilter(field_name="square_feet", lookup_expr='lte')

    class Meta:
        model = Listing
        fields = [
            'q', 'sale_type', 'bed_room', 'bath_room', 'min_price', 'max_price', 'min_square_feet', 'max_square_feet'
        ]

    @staticmethod
    def custom_method_lookup(queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(address__icontains=value) | Q(city__icontains=value) |
            Q(state__icontains=value)
        )
