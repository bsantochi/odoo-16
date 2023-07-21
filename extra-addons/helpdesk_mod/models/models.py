# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskMod(models.Model):
    _inherit = "helpdesk.ticket"

    maintenance_request_id = fields.Many2one(
      string="Peticion de mantenimiento",
      comodel_name="maintenance.request",
      ondelete="restrict",
      store=True,
      copied=True
    )

    product_structure_ids = fields.One2many(
      string='Estructura de productos',
      comodel_name='maintenance.product_list',
      inverse_name='ticket_id',
      store=True,
      copied=True
    )

    @api.onchange("maintenance_request_id")
    def _onchange_maintenance_request_id(self):
        if self.maintenance_request_id:
            self.product_structure_ids = None
            self.product_structure_ids = self.maintenance_request_id.product_structure_ids


