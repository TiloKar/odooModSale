from odoo import models, fields

class Task(models.Model):
  _inherit = 'project.task'

  is_my_employee = fields.Boolean(compute='_compute_is_my_employee',
    help="Technical field to decide whether the task field is editable")

  def _compute_is_my_employee(self):
    self.is_my_employee = True
