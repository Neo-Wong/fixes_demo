from rest_framework import serializers

from . import models as _m
from . import utils as _u


class ImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = _m.Images
        fields = "__all__"

    def update(self, instance, validated_data):
        old_file_path = instance.Url.path
        res = super().update(instance, validated_data)
        _u.delete_upload_file(old_file_path)
        return res


class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(
        source='product_images',
        read_only=True,
        required=False,
        many=True,
    )

    class Meta:
        model = _m.Products
        fields = "__all__"

    def update(self, instance, validated_data):
        old_file_path = instance.logo.path
        res = super().update(instance, validated_data)
        _u.delete_upload_file(old_file_path)
        return res


class VariantModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(
        source='variant_images',
        read_only=True,
        required=False,
        many=True,
    )

    class Meta:
        model = _m.Variants
        fields = "__all__"
