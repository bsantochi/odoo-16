from odoo import models, fields, api

class MaintenancePlan(models.Model):
  _inherit = 'maintenance.plan'

  product_structure_ids=fields.One2many(
  string='Productos para plan de mantenimiento',
  comodel_name='maintenance.product_list',
  inverse_name='maintenance_plan_id',
  store=True,
  copied=True
  )