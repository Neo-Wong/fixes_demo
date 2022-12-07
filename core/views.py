from rest_framework.viewsets import ModelViewSet

from . import filters as _f
from . import models as _m
from . import serializers as _s

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = _m.Products.objects.all()
    serializer_class = _s.ProductModelSerializer
    filterset_class = _f.ProductFilter

    ordering = ('-id', )
    ordering_fields = ('id', 'is_deleted', 'created_at', 'updated_at')
    search_fields = ('$name', '$description')


class VariantViewSet(ModelViewSet):
    queryset = _m.Variants.objects.all()
    serializer_class = _s.VariantModelSerializer
    filterset_class = _f.VariantFilter

    ordering = ('-id', )
    ordering_fields = ('id', 'is_deleted', 'created_at', 'updated_at')
    search_fields = ('$name', '$size', '$color')


class ImageViewSet(ModelViewSet):
    queryset = _m.Images.objects.all()
    serializer_class = _s.ImageModelSerializer
    filterset_class = _f.ImageFilter

    ordering = ('-id', )
    ordering_fields = ('id', 'is_deleted', 'created_at', 'updated_at')
