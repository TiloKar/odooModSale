from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class AccountAccount(models.Model):
    _inherit = 'account.account'

class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'

class AccountMove(models.Model):
    _inherit = 'account.move'

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

class AccountJournal(models.Model):
    _inherit = 'account.journal'

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

class ProductTemplate(models.Model):
    _inherit = 'product.template'

class ProductProduct(models.Model):
    _inherit = 'product.product'

class UomUom(models.Model):
    _inherit = 'uom.uom'

class UomCategory(models.Model):
    _inherit = 'uom.category'

class ResPartner(models.Model):
    _inherit = 'res.partner'

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

class BbiMaterial(models.Model):
    _inherit = 'bbi.material'

class BbiHistory(models.Model):
    _inherit = 'bbi.history'
