from ...vendor import models


def resolve_vendor(id):
    return models.Vendor.objects.filter(id=id).first()


def resolve_vendors():
    return models.Vendor.objects.all()
