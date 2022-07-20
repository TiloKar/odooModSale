from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'
