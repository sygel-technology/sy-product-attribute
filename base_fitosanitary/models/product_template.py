# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    botanic_denomination_id = fields.Many2one(
        string="Botanic Denomination",
        comodel_name="botanic.denomination",
    )
