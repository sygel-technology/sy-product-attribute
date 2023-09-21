# Copyright 2023 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    old_product_id = fields.Integer(
        string='Old Product ID',
    )


class ProductTemplate(models.Model):
    _inherit = "product.template"

    old_product_template_id = fields.Integer(
        string='Old Product Template ID',
    )
