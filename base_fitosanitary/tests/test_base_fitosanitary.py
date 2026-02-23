# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestBaseFitosanitary(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.botanic_denomination = cls.env["botanic.denomination"].create(
            {"name": "Testola Botanicae Denominatia"}
        )
        cls.product = cls.env["product.product"].create(
            {
                "name": "Test product",
                "botanic_denomination_id": cls.botanic_denomination.id,
            }
        )
        cls.env.company.fitosanitary_reference = "Fito-123"
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.pick = cls.env["stock.picking"].create(
            {
                "partner_id": cls.partner.id,
                "picking_type_id": cls.env.ref("stock.picking_type_out").id,
                "state": "draft",
                "move_ids_without_package": [
                    (
                        0,
                        0,
                        {
                            "name": "test_line",
                            "product_id": cls.product.id,
                            "product_uom_qty": 1.0,
                            "quantity": 0.0,
                        },
                    )
                ],
            }
        )

    def test_data(self):
        """Check that the data has been created"""
        self.assertTrue(self.product.botanic_denomination_id)
        self.assertTrue(self.env.company.fitosanitary_reference)

    def test_report(self):
        """Check that the new report renders without failure"""
        report = self.env.ref("base_fitosanitary.stock_fitosanitary_report")
        self.env["ir.actions.report"]._render_qweb_pdf(report.id, res_ids=self.pick.ids)
