# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    def _compute_price_rule_get_items(
        self, products_qty_partner, date, uom_id, prod_tmpl_ids, prod_ids, categ_ids
    ):
        self.ensure_one()
        self.env["product.pricelist.item"].flush(
            ["price", "currency_id", "company_id", "active"]
        )
        products = self.env["product.product"].browse(prod_ids)
        brand_ids = {}
        for p in products:
            brand = p.product_brand_id
            if brand:
                brand_ids[brand.id] = True
        brand_ids = list(brand_ids)
        # Load all rules
        self.env.cr.execute(
            """
            SELECT
                item.id
            FROM
                product_pricelist_item AS item
            LEFT JOIN product_category AS categ ON item.categ_id = categ.id
            WHERE
                (item.product_tmpl_id IS NULL OR item.product_tmpl_id = any(%s))
                AND (item.product_id IS NULL OR item.product_id = any(%s))
                AND (item.categ_id IS NULL OR item.categ_id = any(%s))
                AND (item.applied_on != '2a_product_tags' OR item.id IN
                    (
                        SELECT product_pricelist_item_id
                        FROM product_pricelist_item_product_template_tag_rel AS rel
                        WHERE rel.product_template_tag_id IN
                        (
                            SELECT tag.tag_id
                            FROM product_template_product_tag_rel as tag
                            WHERE tag.product_tmpl_id IN %s
                        )
                    )
                )
                AND (item.brand_id IS NULL OR item.brand_id = any(%s))
                AND (item.pricelist_id = %s)
                AND (item.date_start IS NULL OR item.date_start<=%s)
                AND (item.date_end IS NULL OR item.date_end>=%s)
                AND (item.active = TRUE)
            ORDER BY
                item.applied_on, item.min_quantity desc, categ.complete_name desc, item.id desc
            """,
            (
                prod_tmpl_ids,
                prod_ids,
                categ_ids,
                tuple(prod_tmpl_ids),
                brand_ids,
                self.id,
                date,
                date,
            ),
        )
        item_ids = [x[0] for x in self.env.cr.fetchall()]
        return self.env["product.pricelist.item"].browse(item_ids)
