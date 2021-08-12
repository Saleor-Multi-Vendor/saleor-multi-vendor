import graphene
from .mutations import (
    VendorCreate
)

# registering the mutaion for schema here which takes automatically when 
# run command npm run build-schema
class VendorMutations(graphene.ObjectType):
    create_vendor = VendorCreate.Field()