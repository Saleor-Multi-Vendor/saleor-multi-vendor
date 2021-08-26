import django_filters
from graphene_django.filter import GlobalIDMultipleChoiceFilter

from ...vendor.models import Vendor, VendorWarehouse
from ..core.types import FilterInputObjectType
from ..utils.filters import filter_by_query_param


def prefetch_qs_for_filter(qs):
    return qs.prefetch_related("user")


def filter_search_vendor(qs, _, value):
    search_fields = {
        "shop_name",
        "user__email",
        "user__first_name",
    }
    if value:
        qs = prefetch_qs_for_filter(qs)
        qs = filter_by_query_param(qs, value, search_fields)

    return qs


def filter_search_vendor_warehouse(qs, _, value):
    search_fields = {
        "vendor_id__shop_name",
        "vendor_id__user__email",
        "vendor_id__user__first_name",
        "warehouse__name",
    }
    if value:
        qs = qs.select_related("vendor", "warehouse")
        qs = filter_by_query_param(qs, value, search_fields)

    return qs


class VendorFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method=filter_search_vendor)
    ids = GlobalIDMultipleChoiceFilter(field_name="id")

    class Meta:
        model = Vendor
        fields = []


class VendorFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = VendorFilter


class VendorWarehouseFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method=filter_search_vendor_warehouse)

    class Meta:
        model = VendorWarehouse
        fields = []


class VendorWarehouseFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = VendorWarehouseFilter
