# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Product Lst Price Calculate",
    "summary": "Calculate product sales price according to cost and expected margin",
    "version": "15.0.1.0.0",
    "category": "Product",
    "website": "https://www.sygel.es",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
    ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/product_views.xml",
    ],
}
