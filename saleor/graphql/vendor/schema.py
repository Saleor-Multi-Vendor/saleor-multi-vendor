import graphene

from ..core.fields import FilterInputConnectionField
from ..core.utils import from_global_id_or_error
from .filters import VendorFilterInput, VendorWarehouseFilterInput
from .mutations import (
    VendorCreate,
    VendorDelete,
    VendorUpdate,
    VendorWarehouseCreate,
    VendorWarehouseDelete,
    VendorWarehouseUpdate,
)
from .resolvers import (
    resolve_vendor,
    resolve_vendor_warehouse,
    resolve_vendor_warehouses,
    resolve_vendors,
)
from .sorters import VendorSortingInput
from .types import Vendor, VendorWarehouse


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

    vendors = FilterInputConnectionField(
        Vendor,
        description="List of vendors.",
        filter=VendorFilterInput(),
        sort_by=VendorSortingInput(),
    )

    def resolve_vendor(self, info, **data):
        vendor_pk = data.get("id")
        _, id = from_global_id_or_error(vendor_pk, Vendor)
        return resolve_vendor(id)

    def resolve_vendors(self, info, **_kwargs):
        return resolve_vendors()


class VendorWarehouseQueries(graphene.ObjectType):
    vendor_warehouse = graphene.Field(
        VendorWarehouse,
        description="Look up vendor's warehouse by ID.",
        id=graphene.ID(required=True, description="ID of a vendor"),
    )
    vendor_warehouses = FilterInputConnectionField(
        VendorWarehouse,
        description="List of vendor warehouses.",
        filter=VendorWarehouseFilterInput(),
    )

    def resolve_vendor_warehouse(self, info, **data):
        vendor_warehouse_id = data.get("id")
        _, id = from_global_id_or_error(vendor_warehouse_id, VendorWarehouse)
        return resolve_vendor_warehouse(id)

    def resolve_vendor_warehouses(self, info, **_kwargs):
        return resolve_vendor_warehouses()
