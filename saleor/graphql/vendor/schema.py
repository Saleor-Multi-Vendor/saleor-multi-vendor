import graphene

from ..core.utils import from_global_id_or_error
from .filters import VendorFilterInput
from .mutations import (
    VendorCreate,
    VendorDelete,
    VendorUpdate,
    VendorWarehouseCreate,
    VendorWarehouseDelete,
    VendorWarehouseUpdate,
)
from .resolvers import resolve_vendor, resolve_vendors
from .types import Vendor


# registering the mutaion for schema here which takes automatically when
# run command npm run build-schema
class VendorMutations(graphene.ObjectType):
    create_vendor = VendorCreate.Field()
    delete_vendor = VendorDelete.Field()
    update_vendor = VendorUpdate.Field()


class VendorWarehouseMutation(graphene.ObjectType):
    create_vendorWarehouse = VendorWarehouseCreate.Field()
    update_vendorWarehouse = VendorWarehouseUpdate.Field()
    delete_vendorWarehouse = VendorWarehouseDelete.Field()


class VendorQueries(graphene.ObjectType):
    vendor = graphene.Field(
        Vendor,
        description="Look up a vendor by ID.",
        id=graphene.Argument(graphene.ID, description="ID of a vendor", required=True),
    )

    vendors = graphene.Field(
        Vendor, description="List of vendors.", filter=VendorFilterInput()
    )

    def resolve_vendor(self, info, **data):
        vendor_pk = data.get("id")
        _, id = from_global_id_or_error(vendor_pk, Vendor)
        return resolve_vendor(id)

    def resolve_vendors(self, info, **_kwargs):
        return resolve_vendors()
