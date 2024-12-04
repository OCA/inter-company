# Copyright 2022 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging

from odoo import fields, models

from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class OdooPaymentProviderError(models.Model):
    _queue_priority = 10
    _name = "odoo.payment.provider.error"
    _inherit = ["odoo.binding"]
    _inherits = {"payment.provider.error": "odoo_id"}
    _description = "Odoo Payment Provider Error"
    _sql_constraints = [
        (
            "external_id",
            "UNIQUE(external_id)",
            "External ID (external_id) must be unique!",
        ),
    ]

    def resync(self):
        if self.backend_id.main_record == "odoo":
            raise NotImplementedError
        else:
            return self.delayed_import_record(
                self.backend_id, self.external_id, force=True
            )


class PaymentProviderError(models.Model):
    _inherit = "payment.provider.error"

    bind_ids = fields.One2many(
        comodel_name="odoo.payment.provider.error",
        inverse_name="odoo_id",
        string="Odoo Bindings",
    )


class PaymentProviderErrorAdapter(Component):
    _name = "odoo.payment.provider.error.adapter"
    _inherit = "odoo.adapter"
    _apply_on = "odoo.payment.provider.error"

    _odoo_model = "payment.provider.error"

    # Set get_passive to True to get the passive records also.
    _get_passive = False
