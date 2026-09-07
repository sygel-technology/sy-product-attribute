# Copyright 2023 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    country_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
    )


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends("product_tmpl_id.country_id", "name")
    def _compute_display_name(self):
        res = super()._compute_display_name()
        for product in self.filtered(lambda x: x.product_tmpl_id.country_id):
            if not self.env.context.get("no_country", False):
                product.display_name = f"{product.display_name} ({product.product_tmpl_id.country_id.name})"  # noqa E501
        return res

    @api.model
    def _name_search(self, name, domain=None, operator="ilike", limit=None, order=None):
        product_ids = super()._name_search(name, domain, operator, limit, order)
        if name:
            limit_search = limit
            if not limit and product_ids:
                limit_search = len(product_ids)
            elif limit and product_ids:
                limit_search -= len(product_ids)
            if not limit_search or limit_search > 0:
                product_ids += self._search(
                    [
                        ("product_tmpl_id.country_id", "ilike", name),
                        ("id", "not in", product_ids),
                    ],
                    limit=limit_search,
                )
        return product_ids
