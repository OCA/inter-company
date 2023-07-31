# Copyright 2013-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import logging

from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping, only_create

_logger = logging.getLogger(__name__)


class ProductAttributeImporter(Component):
    """Import Odoo UOM"""

    _name = "odoo.product.attribute.importer"
    _inherit = "odoo.importer"
    _apply_on = "odoo.product.attribute"


class ProductAttributeMapper(Component):
    _name = "odoo.product.attribute.mapper"
    _inherit = "odoo.import.mapper"
    _apply_on = "odoo.product.attribute"

    direct = [
        ("name", "name"),
        ("create_variant", "create_variant"),
        ("allow_filling", "allow_filling"),
        ("visibility", "visibility"),
    ]

    @only_create
    @mapping
    def check_att_exists(self, record):
        # Todo: bu çalışmıyor ki? dict'e odoo_id ekliyor ama yine de create ediyor duplicate oluyor
        # TODO: Improve and check family, factor etc...
        domain = [("name", "=", record["name"])]
        if create_variant := record.get("create_variant"):
            domain.append(("create_variant", "=", create_variant))
        att_id = self.env["product.attribute"].search(domain)
        res = {}
        if len(att_id) == 1:
            res.update({"odoo_id": att_id.id})

        return res

    @mapping
    def create_variant(self, record):
        res = {"create_variant": "no_variant"}
        if record.get("create_variant") == "always":
            res.update(create_variant="always")
        return res
