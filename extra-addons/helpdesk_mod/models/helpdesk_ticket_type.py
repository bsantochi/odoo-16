from odoo import models, fields, api


class HelpdeskMod(models.Model):
    _inherit = "helpdesk.ticket.type"

    access_group = fields.Selection([('0', 'Usuario Interno'), ('1', 'Usuario Portal'), ('2', 'Todos')], 'Permiso de acceso', default="2")