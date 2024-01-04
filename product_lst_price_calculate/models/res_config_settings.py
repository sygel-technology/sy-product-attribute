# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    apply_product_min_margin = fields.Boolean(
        string="Apply Product Min. Margin",
        related="company_id.apply_product_min_margin",
        readonly=False
    )
    product_min_margin = fields.Float(
        string="Product Min. Margin (%)",
        related="company_id.product_min_margin",
        digits="Product Price",
        readonly=False
    )
