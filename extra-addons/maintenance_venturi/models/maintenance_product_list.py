# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MaintenanceProductList(models.Model):
    _inherit = "maintenance.product_list"

    ticket_id = fields.Many2one('helpdesk.ticket', string="Ticket")
