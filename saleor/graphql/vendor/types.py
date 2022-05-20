import graphene

from ...vendor import models
from ..core.connection import CountableDjangoObjectType


# Basic input required for vendor
class VendorInput(graphene.InputObjectType):
    slug = graphene.String(decription="Slug")


# More input fields for create required.
class VendorCreateInput(VendorInput):
    shop_name = graphene.String(description="Shop Name")
    user = graphene.ID(description="User id")


# This might be for response is requried
class Vendor(CountableDjangoObjectType):
    class Meta:
        description = "Represents Vendor"
        model = models.Vendor
        interfaces = [graphene.relay.Node]
        only_fields = [
            "id",
            "slug",
            "shop_name",
            "user",
            # "allocation"
        ]


# input fields for create required.
class VendorWarehouseInput(graphene.InputObjectType):
    vendor_id = graphene.ID(description="Vendor Id")
    warehouse = graphene.ID(description="warehouse  id", required=False)


# This is the response on submit.
class VendorWarehouse(CountableDjangoObjectType):
    class Meta:
        description = "Represents VendorWarehoue"
        model = models.VendorWarehouse
        interfaces = [graphene.relay.Node]
        only_fields = ["id", "vendor_id", "warehouse"]
