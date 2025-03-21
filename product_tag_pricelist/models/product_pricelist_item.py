# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    applied_on = fields.Selection(
        selection_add=[('2a_product_tags', 'Product Tags')],
        ondelete={"2a_product_tags": "set default"},
    )
    product_tag_ids = fields.Many2many(
        comodel_name='product.template.tag',
        string="Product Tags"
    )
    # This field is stored to keep the sorting rules as two
    # different queries are used
    categ_name = fields.Char(
        string="Categ Name",
        related="categ_id.complete_name",
        store=True
    )

    @api.constrains('product_id', 'product_tmpl_id', 'categ_id', 'product_tag_ids')
    def _check_product_consistency(self):
        for item in self:
            if item.applied_on == "2a_product_tags" and not item.product_tag_ids:
                raise ValidationError(_("Please specify the product tags for which this rule should be applied"))

    @api.depends('applied_on', 'categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
        'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge', 'product_tag_ids')
    def _get_pricelist_item_name_price(self):
        super()._get_pricelist_item_name_price()
        for item in self:
            if item.product_tag_ids and item.applied_on == '2a_product_tags':
                tag_names = item.product_tag_ids.mapped('name')
                tag_names_str = ', '.join(tag_names)
                item.name = _("Tags: %s") % (tag_names_str)

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if values.get('applied_on', False):
                # Ensure item consistency for later searches.
                applied_on = values['applied_on']
                if applied_on == '3_global':
                    values.update(dict(product_tag_ids=False))
                elif applied_on == '2a_product_tags':
                    values.update(dict(product_id=None, product_tmpl_id=None, categ_id=None))
                elif applied_on == '2_product_category':
                    values.update(dict(product_tag_ids=False))
                elif applied_on == '1_product':
                    values.update(dict(product_tag_ids=False))
                elif applied_on == '0_product_variant':
                    values.update(dict(product_tag_ids=False))
        return super(PricelistItem, self).create(vals_list)

    def write(self, values):
        if values.get('applied_on', False):
            applied_on = values['applied_on']
            if applied_on == '3_global':
                values.update(dict(product_tag_ids=False))
            elif applied_on == '2a_product_tags':
                values.update(dict(product_id=None, product_tmpl_id=None, categ_id=None))
            elif applied_on == '2_product_category':
                values.update(dict(product_tag_ids=False))
            elif applied_on == '1_product':
                values.update(dict(product_tag_ids=False))
            elif applied_on == '0_product_variant':
                values.update(dict(product_tag_ids=False))
        return super(PricelistItem, self).write(values)
