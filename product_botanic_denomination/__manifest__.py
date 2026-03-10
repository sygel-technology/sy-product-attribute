# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Botanic Denomination",
    "summary": "Add the product botanic denomination to products",
    "version": "18.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/sygel-technology/sy-product-attribute",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/botanic_denomination_views.xml",
        "views/product_views.xml",
    ],
}
