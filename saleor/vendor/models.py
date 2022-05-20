from django.conf import settings
from django.db import models

from saleor.core.permissions import VendorPermissions

# Create your models here.
from ..warehouse.models import Warehouse


class Vendor(models.Model):
    """Model definition for Vendor."""

    # TODO: Define fields here
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        # blank=True,
        # null=True,
        related_name="vendor_user",
        on_delete=models.CASCADE,
    )
    # here the ideas clash
    # one django doesn't have onetomany only manytoone
    # so either I make vendor foreign key in warehouse
    # or here is a dirty little trick to make manytomany
    # into one to many

    # allocation = models.ManyToManyField(Allocation, related_name="vendor_allocation")
    shop_name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    # def save(self, *args, **kwargs):
    #     if Vendor.objects.get(warehouse=self.warehouse):
    #         raise Exception("This number has been used.")
    #         return super(Vendor, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Vendor."""

        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        permissions = (
            (
                VendorPermissions.MANAGE_VENDOR.codename,
                "Manage Vendor.",
            ),
        )

    def __str__(self):
        """Unicode representation of Vendor."""
        return self.shop_name


class VendorWarehouse(models.Model):
    vendor_id = models.ForeignKey(
        Vendor, related_name="vendorware_vendor", on_delete=models.CASCADE
    )
    warehouse = models.OneToOneField(
        Warehouse, related_name="vendor_warehouse", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "VendorWarehouse"
        verbose_name_plural = "VendorWarehouses"

    def __str__(self):
        return str(self.vendor_id)
