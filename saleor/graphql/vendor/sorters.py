import graphene

from ..core.types import SortInputObjectType


class VendorSortField(graphene.Enum):
    NAME = ["shop_name", "slug"]

    @property
    def description(self):
        if self.shop_name in VendorSortField.__enum__.member_names_:
            sort_name = self.shop_name.lower().replace("_", " ")
            return f"Sort vendors by {sort_name}."
        raise ValueError("Unsupported enum value: %s" % self.value)


class VendorSortingInput(SortInputObjectType):
    class Meta:
        sort_enum = VendorSortField
        type_name = "vendors"
