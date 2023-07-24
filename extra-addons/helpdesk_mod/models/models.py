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

