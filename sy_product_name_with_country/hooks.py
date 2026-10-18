# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


def pre_init_hook(env):
    openupgrade.update_module_names(
        env.cr,
        [("product_name_with_country", "sy_product_name_with_country")],
        merge_modules=True,
    )
