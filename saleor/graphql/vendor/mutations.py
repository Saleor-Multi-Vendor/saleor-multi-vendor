from re import L
import graphene
from ..account.i18n import I18nMixin
from ...core.permissions import VendorPermissions
from ..core.mutations import ModelDeleteMutation, ModelMutation
from ..core.types.common import VendorError
from .types import VendorCreateInput, VendorWarehouseInput
from ...vendor import models

# to create vendor which is registered in schema
class VendorCreate(ModelMutation, I18nMixin):
    class Arguments:
        input = VendorCreateInput(
            required=True, description="Fields required to create vendor."
        )

    class Meta:
        description = "Create new Vendor"
        model = models.Vendor
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"


class VendorUpdate(VendorCreate):
    class Arguments:
        id = graphene.ID(required=True, description="ID of a vendor")
        input = VendorCreateInput(
            required=True, description="Fields required to Update vendor."
        )

    class Meta:
        description = "Update new Vendor"
        model = models.Vendor
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"

class VendorDelete(ModelDeleteMutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of a vendor")
    
    class Meta:
        description = "Delete a vendor"
        model = models.Vendor
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"

class VendorWarehouseCreate(ModelMutation, I18nMixin):
    class Arguments:
        input = VendorWarehouseInput(
            required=True, description="Fields required to create vendor."
        )

    class Meta:
        description = "Create new Vendor Warehouse"
        model = models.VendorWarehouse
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"

class VendorWarehouseUpdate(VendorWarehouseCreate):

    class Arguments:
        id = graphene.ID(required=True, description="ID of a vendorWarehouse")
        input = VendorWarehouseInput(
            required=True, description="Fields required to update vendor."
        )

    class Meta:
        description = "Update new Vendor Warehouse"
        model = models.VendorWarehouse
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"

class VendorWarehouseDelete(ModelDeleteMutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID of a vendorWarehouse")

    class Meta:
        description = "Delete new Vendor Warehouse"
        model = models.VendorWarehouse
        permissions = (VendorPermissions.MANAGE_VENDOR,)
        error_type_class = VendorError
        error_type_field = "vendor_errors"