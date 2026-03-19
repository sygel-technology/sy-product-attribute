# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BotanicDenomination(models.Model):
    _name = "botanic.denomination"
    _description = "Botanic denomination for products"

    name = fields.Char()
