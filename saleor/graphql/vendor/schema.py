import graphene
from .mutations import (
    VendorCreate,
    VendorDelete,
    VendorUpdate,
    VendorWarehouseCreate,
    VendorWarehouseDelete,
    VendorWarehouseUpdate
)

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