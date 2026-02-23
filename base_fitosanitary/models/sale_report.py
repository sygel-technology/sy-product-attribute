# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


# TODO: Mover a otro modulo
class SaleReport(models.Model):
    _inherit = "sale.report"

    botanic_denomination_id = fields.Many2one(
        string="Botanic Denomination",
        comodel_name="botanic.denomination",
    )

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """
            ,t.botanic_denomination_id"""
        return res

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["botanic_denomination_id"] = "t.botanic_denomination_id"
        return res
