from django_filters.rest_framework import FilterSet
from . import models as _m

# Field lookups expression
BOOL_EXPR = ('exact',)
CHAR_EXPR = (
    'exact',
    'iexact',
    'startswith',
    'istartswith',
    'endswith',
    'iendswith',
    'contains',
    'icontains',
)
DATE_TIME_EXPR = (
    'exact',
    'year',
    'year__gt',
    'year__lt',
    'month',
    'month__gt',
    'month__lt',
    'day',
    'day__gt',
    'day__lt',
)
FOREIGN_KEY_EXPR = ('exact',)


class ProductFilter(FilterSet):
    class Meta:
        model = _m.Products
        fields = {
            'name': CHAR_EXPR,
            'created_at': DATE_TIME_EXPR,
            'updated_at': DATE_TIME_EXPR,
            'is_deleted': BOOL_EXPR,
        }


class VariantFilter(FilterSet):
    class Meta:
        model = _m.Variants
        fields = {
            'name': CHAR_EXPR,
            'color': CHAR_EXPR,
            'size': CHAR_EXPR,
            'created_at': DATE_TIME_EXPR,
            'updated_at': DATE_TIME_EXPR,
            'is_deleted': BOOL_EXPR,
        }


class ImageFilter(FilterSet):
    class Meta:
        model = _m.Images
        fields = {
            'product': FOREIGN_KEY_EXPR,
            'variant': FOREIGN_KEY_EXPR,
            'created_at': DATE_TIME_EXPR,
            'updated_at': DATE_TIME_EXPR,
            'is_deleted': BOOL_EXPR,
        }
