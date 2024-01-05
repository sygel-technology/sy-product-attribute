# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    lst_price_calculation = fields.Float(
        string="Sale Price Calculation",
        digits="Product Price",
    )
    cost_calculation = fields.Float(
        string="Cost Calculation",
        digits="Product Price",
        compute="_compute_cost_calculation",
        help="Cost Calculation is [ Vendor Price Calculation * (1 - Vendor "
        "Discount Calculation / 100) ].",
        store=True
    )
    vendor_price_calculation = fields.Float(
        string="Vendor Price Calculation",
        digits="Product Price"
    )
    vendor_discount_calculation = fields.Float(
        string="Vendor Discount Calculation",
        digits="Product Price"
    )
    theorical_margin_calculation = fields.Float(
        compute="_compute_margin_calculation",
        string="Theorical Margin Calculation",
        digits="Product Price",
        store=True,
        help="Theorical Margin Calculation "
        "[ Sale Price Calculation - Cost Calculation ]."
    )
    standard_margin_rate_calculation = fields.Float(
        compute="_compute_margin_calculation",
        string="Theorical Margin Calculation (%)",
        digits="Product Price",
        readonly=False,
        store=True,
        help="Theorical Margin Calculation (%) "
        "[ (Sale Price Calculation - Cost Calculation) / Sale Price "
        "Calculation * 100]. If no Sale Price Calculation and Cost "
        "Calculation set, will display 999.0",
    )
    min_margin_rate = fields.Float(
        string="Min. Margin Rate",
        compute="_compute_min_margin_rate"
    )    

    @api.depends("company_id")
    def _compute_min_margin_rate(self):
        for sel in self:
            min_margin_rate = 0.0
            company = sel.company_id or self.env.company
            if company.apply_product_min_margin:
                min_margin_rate = company.product_min_margin
            sel.min_margin_rate = min_margin_rate

    @api.depends(
        "lst_price_calculation",
        "cost_calculation",
        "vendor_price_calculation",
        "vendor_discount_calculation"
    )
    def _compute_margin_calculation(self):
        for product in self:
            product.theorical_margin_calculation = product.lst_price_calculation - product.cost_calculation
            if product.lst_price_calculation == 0:
                company = product.company_id or self.env.company
                product.standard_margin_rate_calculation = company.product_margin_calculation_default or 999.0
            else:
                product.standard_margin_rate_calculation = (
                    (product.lst_price_calculation - product.cost_calculation)
                    / product.lst_price_calculation
                    * 100
                )

    @api.depends(
        "vendor_price_calculation",
        "vendor_discount_calculation"
    )
    def _compute_cost_calculation(self):
        for product in self:
            product.cost_calculation = product.vendor_price_calculation * (1 - product.vendor_discount_calculation / 100)

    @api.onchange("standard_margin_rate_calculation")
    def _onchange_standard_margin_rate_calculation(self):
        if self.standard_margin_rate_calculation != 100:
            self.lst_price_calculation = self.cost_calculation / (
                1 - self.standard_margin_rate_calculation / 100
            )
        company = self.company_id or self.env.company
        if company.apply_product_min_margin and self.standard_margin_rate_calculation < company.product_min_margin:
            return {
                'warning': {
                    'title': _("Margin Calculation Warning"),
                    'message': _("The minimum product margin set in company is {}%.".format(
                        company.product_min_margin
                    )),
                }
            }

    @api.onchange("vendor_price_calculation")
    def _onchange_vendor_price_calculation(self):
        if self.standard_margin_rate_calculation != 100:
            self.lst_price_calculation = self.cost_calculation / (
                1 - self.standard_margin_rate_calculation / 100
            )

    def action_transfer_lst_price_calculation(self):
        for product in self:
            product.write({
                "list_price": product.lst_price_calculation
            })
