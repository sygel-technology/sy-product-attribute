# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestProductBotanicDenomination(TransactionCase):
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

    def test_data(self):
        """Check that the data has been created"""
        self.assertTrue(self.product.botanic_denomination_id)
