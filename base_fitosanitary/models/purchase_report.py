# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.tools import SQL


# TODO: Mover a otro modulo
class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    botanic_denomination_id = fields.Many2one(
        string="Botanic Denomination",
        comodel_name="botanic.denomination",
    )

    def _select(self):
        return SQL(
            "%s, t.botanic_denomination_id as botanic_denomination_id",
            super()._select(),
        )

    def _group_by(self):
        return SQL("%s,t.botanic_denomination_id", super()._group_by())
