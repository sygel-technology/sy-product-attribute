# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Fitosanitary",
    "summary": "Base Fitosanitary",
    "version": "18.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/sygel-technology/sy-product-attribute",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # 'product',
        "stock",
        "sale",
        "purchase",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/botanic_denomination_views.xml",
        "views/fitosanitary_report.xml",
        "views/product_views.xml",
        "views/res_company_views.xml",
    ],
}
