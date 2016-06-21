import logging

from rest_framework import serializers
from .models import ProductClass, ProductGroup, ProductClassContent, ContentCategory

logger = logging.getLogger(__name__)


class ProductClassSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = ProductClass

        fields = (
            'id',
            'pcl_name',
            'pcl_display_name',
            'pcl_is_system'
        )


class ProductGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductGroup

        fields = (
            'id',
            'pgr_name',
            'pgr_display_name',
            'is_catalog'
        )


class ProductClassContentSerializer(serializers.HyperlinkedModelSerializer):
    pcc_class = serializers.PrimaryKeyRelatedField(
        queryset=ProductClass.objects.all(), many=False)

    pcc_category = serializers.PrimaryKeyRelatedField(
        queryset=ContentCategory.objects.all(), many=False)

    class Meta:
        model = ProductClassContent

        fields = (
            'id',
            'pcc_class',
            'pcc_category',
            'pcc_name',
            'pcc_display_name',
            'pcc_ucd',
            'pcc_unit',
            'pcc_reference',
            'pcc_mandatory'
        )
