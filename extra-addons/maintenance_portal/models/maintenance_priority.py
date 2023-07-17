from odoo import fields, models, api
from odoo.http import request

class MaintenancePriority(models.Model):
    _name = "maintenance.maintenance_priority"
    _description = "Prioridad de mantenimiento"
    _order = 'sequence, id'

    name = fields.Text(string="Nombre")
    sequence = fields.Integer('Sequence', default=20)