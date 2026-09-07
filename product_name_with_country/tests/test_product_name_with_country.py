# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestProductNameWithCountry(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.country_spain = cls.env.ref("base.es")
        cls.country_france = cls.env.ref("base.fr")
        cls.product_spain = cls.env["product.product"].create(
            {
                "name": "Test Product Spain",
                "country_id": cls.country_spain.id,
            }
        )
        cls.product_france = cls.env["product.product"].create(
            {
                "name": "Test Product France",
                "country_id": cls.country_france.id,
            }
        )
        cls.product_no_country = cls.env["product.product"].create(
            {
                "name": "Test Product No Country",
            }
        )

    def test_display_name_with_country(self):
        self.assertIn(
            self.country_spain.name,
            self.product_spain.display_name,
        )
        self.assertEqual(
            self.product_spain.display_name,
            f"Test Product Spain ({self.country_spain.name})",
        )

    def test_display_name_without_country(self):
        self.assertEqual(
            self.product_no_country.display_name,
            "Test Product No Country",
        )

    def test_display_name_with_no_country_context(self):
        product = self.product_spain.with_context(no_country=True)
        self.assertEqual(
            product.display_name,
            "Test Product Spain",
        )

    def test_name_search_by_country(self):
        product_ids = self.env["product.product"]._name_search(self.country_spain.name)
        self.assertIn(self.product_spain.id, product_ids)
        self.assertNotIn(self.product_france.id, product_ids)

    def test_name_search_by_product_name(self):
        product_ids = self.env["product.product"]._name_search("Test Product Spain")
        self.assertIn(self.product_spain.id, product_ids)
