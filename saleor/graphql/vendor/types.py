import graphene
from ..core.connection import CountableDjangoObjectType
from ...vendor import models

# Basic input required for vendor
class VendorInput(graphene.InputObjectType):
    shop_name = graphene.String(description="Shop Name")

# More input fields for create required.
class VendorCreateInput(VendorInput):
    pass

# This might be for response is requried 
class Vendor(CountableDjangoObjectType):
    
    class Meta:
        description = "Represents Vendor"
        model = models.Vendor
        interfaces = [graphene.relay.Node]
        only_fields = [
            "id",
            "shop_name"
        ]