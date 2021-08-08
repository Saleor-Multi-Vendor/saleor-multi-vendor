from django.conf import settings
from django.db import models

# Create your models here.
from ..warehouse.models import Allocation, Warehouse


class Vendor(models.Model):
    """Model definition for Vendor."""

    # TODO: Define fields here
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="vendor",
        on_delete=models.CASCADE,
    )
    # here the ideas clash
    # one django doesn't have onetomany only manytoone
    # so either I make vendor foreign key in warehouse
    # or here is a dirty little trick to make manytomany
    # into one to many
    warehouse = models.ManyToManyField(Warehouse, related_name="vendors")
    allocation = models.ManyToManyField(Allocation, related_name="vendors")
    shop_name = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        if Vendor.objects.get(warehouse=self.warehouse):
            raise Exception("This number has been used.")
            return super(Vendor, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Vendor."""

        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def __str__(self):
        """Unicode representation of Vendor."""
        return self.vendor_name
