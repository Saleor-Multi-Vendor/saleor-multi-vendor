# Saleor Multi Vendor (Marketplace) Addon
Multi Vendor Plugin for Saleor e-Commerce

# [Live Chat at Gitter](https://gitter.im/Saleor-Multi-Vendor/community)
# [Project Board at Github](https://github.com/Saleor-Multi-Vendor/saleor-multi-vendor/projects/1)
# Donate to this project on [Open Collective](https://opencollective.com/saleor-marketplace#category-BUDGET)

## There is no stable release yet. Get help on gitter chat.

## We are looking for contributors. Use issues to get an invite to organization. 

Short Analysis:

Pre-requirements.
- There isn't a latitude or longitude anywhere. Coordinates are required to calculate shipping cost. - We need to record all the product information to order_line to ensure seller send right product and be able to check product properties and photos recorded at checkout time.

Multi Vendor Plugin Implementation

Let's check a success plugin in ruby ecosystem and learn best practices. [Spree Multi Vendor Plugin](https://github.com/spree-contrib/spree_multi_vendor)

Let's start with database.
![ERD](https://user-images.githubusercontent.com/9559372/85078411-0fd12c00-b1cd-11ea-95ae-da0574904242.png)

We already know the Saleor feature set but database shows what actually happening.

Defining the feature set for Vendors:
- Which features are belong to the super admin?
- Which features are belong to the vendor?

Methodology:
- Using polymorphism.
- Using vendor scope
- Using vendor role

Pluses:
- Current warehouse system:
With current warehouse system our implementation will be more easy. Because each vendor will have at least one warehouse. So we don't need to modify all the application. We only to add some foreign keys to db and creating a little code as plugin.

A marketplace requirement at production:
- Vendor data management in dashboard by super admin or vendor's own. Such as name, profile picture, company details, payout account, etc.
- Stripe Connect as payment integration to control payments and refunds.
- A product can be posted by several vendors. We can have same variants from different vendors. We need to be able to make price comparison and show other sellers price.

Technical equality of these requirements.
- Stripe Connect gateway
- State machine for payments
- Vendor_Id as scope in products, variants, variant_photos, order_items, fulfillments
- Custom logic described below.

Application logic:

General:
- The vendor role will only have permissions to manage their orders and shippings.
- All the order items, shippings, fulfillments must be grouped for each vendor in the order.
- Vendor's fulfillments will be already done with current warehouse logic.
- Buttons to change fulfillment status to move payment across buyer and seller.

Dashboard:
- If a user have vendor role the controllers use the vendor_id to filter scope and only return vendor's data. Eg: Vendors will only see their orders and shippings.

Store Front
- We must be able to use vendor_id as filter.
- Product page must show the vendor's name.

So as you can see in spree plugin, this implementation can be done with less than 1000 line of code. I am Ruby on Rails expert, never tried Django before. But I am super impressed to use Saleor as marketplace. If anybody want to work on this feature, we can schedule our times. Thank you!
