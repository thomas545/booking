from django_filters.rest_framework import FilterSet, filters
from .models import Realty


class RealtyFilters(FilterSet):
    price = filters.RangeFilter(field_name='price')

    class Meta:
        model = Realty
        fields = ('price',)