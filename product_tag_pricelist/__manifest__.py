# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Tag Pricelist",
    "summary": "Use tags in pricelists",
    "version": "14.0.1.0.0",
    "category": "Stock",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
        "product_template_tags",
    ],
    "data": [
        "views/product_pricelist_views.xml",
    ],
}
