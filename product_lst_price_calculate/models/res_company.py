# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    apply_product_min_margin = fields.Boolean(
        string="Apply Product Min. Margin"
    )
    product_min_margin = fields.Float(
        string="Product Min. Margin (%)",
        digits="Product Price",
    )
