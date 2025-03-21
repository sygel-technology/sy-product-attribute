# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.onchange("tag_ids")
    def _onchange_tag_ids(self):
        if self.tag_ids:
            return {
                'warning': {
                    'title': _('Product tags have been modified.'),
                    'message': _(
                        'Be aware that sale pricelists will be applied if a '
                        'product tag matches a tag selected in the pricelist.'
                    )
                }
            }
