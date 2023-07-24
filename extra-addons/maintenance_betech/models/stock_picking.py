# -*- coding: utf-8 -*-

from odoo import models, fields, api, Command

class Picking(models.Model):
  _inherit = "stock.picking"

  maintenance_req_id = fields.Many2one(
    comodel_name="maintenance.request",
    string="Mantenimiento relacionado",
    store=True,
    copied=True,
    ondelete="restrict"
  )

  @api.onchange("maintenance_req_id")
  def _maintenance_req_id_on_change(self):
    if self.maintenance_req_id.id:
      self.move_ids_without_package = [(5, 0, 0)]
      for rec in self.maintenance_req_id['product_structure_ids']:
        self.move_ids_without_package = [(0,0, {
          'product_id': rec.product_id.id,
          'product_uom_qty': rec.quantity,
          'product_uom': rec.unit_of_measurement,
          'name': "Product",
          'location_id': self.location_id,
          'location_dest_id': self.location_dest_id
        })]