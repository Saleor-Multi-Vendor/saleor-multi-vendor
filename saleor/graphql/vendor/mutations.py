from ..account.i18n import I18nMixin
from ...core.permissions import VendorPermissions
from ..core.mutations import ModelMutation
from ..core.types.common import VendorError
from .types import VendorCreateInput
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