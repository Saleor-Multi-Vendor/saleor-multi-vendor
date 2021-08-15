import graphene
from django.core.exceptions import ValidationError

from ...core.permissions import VendorPermissions
from ..core.utils import validate_slug_and_generate_if_needed
from ...vendor import models
from ...vendor.error_codes import VendorErrorCode
from ..account.i18n import I18nMixin
from ..core.mutations import ModelDeleteMutation, ModelMutation
from ..core.types.common import VendorError
from .types import VendorCreateInput, VendorWarehouseInput


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
    
    @classmethod
    def clean_input(cls, info, instance, data):
        cleaned_input = super().clean_input(info, instance, data)
        try:
            cleaned_input = validate_slug_and_generate_if_needed(
                instance, "shop_name", cleaned_input
            )
        except ValidationError as error:
            error.code = VendorErrorCode.REQUIRED.value
            raise ValidationError({"slug":error})
        return cleaned_input


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