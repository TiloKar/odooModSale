from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    webshop = fields.Boolean(
        str='WS',
        default=False,
        help='Check this, if product is sold via bbi webshop',
        store=True,
        readonly=False,)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_product_multiline_description_sale(self):
            """ Compute a multiline description of this product, in the context of sales
                    (do not use for purchases or other display reasons that don't intend to use "description_sale").
                It will often be used as the default description of a sale order line referencing this product.

                [MOD]Nur noch Sale description oder leer, kein Name mehr

            """
            name = '';
            if self.description_sale:
                name = self.description_sale

            return name

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def get_sale_order_line_multiline_description_sale(self, product):
        """ Compute a default multiline description for this sales order line.
        In most cases the product description is enough but sometimes we need to append information that only
        exists on the sale order line itself.
        e.g:
        - custom attributes and attributes that don't create variants, both introduced by the "product configurator"
        - in event_sale we need to know specifically the sales order line as well as the product to generate the name:
          the product is not sufficient because we also need to know the event_id and the event_ticket_id (both which belong to the sale order line).

        [MOD]Nur noch Übernahme des Sale Notizfeldes

        """
        return product.get_product_multiline_description_sale()
