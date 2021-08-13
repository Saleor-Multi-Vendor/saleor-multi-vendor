import graphene
from ..core.connection import CountableDjangoObjectType
from ...vendor import models

# Basic input required for vendor
class VendorInput(graphene.InputObjectType):
    slug = graphene.String(decription="Slug")

# More input fields for create required.
class VendorCreateInput(VendorInput):
    shop_name = graphene.String(description="Shop Name")

# This might be for response is requried 
class Vendor(CountableDjangoObjectType):
    
    class Meta:
        description = "Represents Vendor"
        model = models.Vendor
        interfaces = [graphene.relay.Node]
        only_fields = [
            "id",
            "slug",
            "shop_name"
        ]