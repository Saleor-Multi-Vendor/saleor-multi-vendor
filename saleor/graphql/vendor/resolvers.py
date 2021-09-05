from ...vendor import models


def resolve_vendor(id):
    return models.Vendor.objects.filter(id=id).first()


def resolve_vendors():
    return models.Vendor.objects.all()


def resolve_vendor_warehouse(id):
    return models.VendorWarehouse.objects.filter(id=id).first()


def resolve_vendor_warehouses():
    return models.VendorWarehouse.objects.all()
