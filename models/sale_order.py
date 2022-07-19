from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

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

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    bbi_project_id = fields.Char(string = 'bbi_project_id')

    isInSitu = fields.Boolean(
        string = 'isInSitu',
        default=False,
        help='Check this, if template product tree should be created for a in situ project',
        readonly=False,)

    def createProjectProductTree(self):
        if not self.bbi_project_id:
            raise ValidationError("Projektnummer muss vergeben werden!")
        self.createProjectProductTreeLevel0()

    #project root
    def createProjectProductTreeLevel0(self):

        vals = []
        vals.append({'name': "{}-Projekt".format(self.bbi_project_id)})

        for p in vals:
            p['detailed_type'] = "product"
            p['type'] = "product"
            p['purchase_ok'] = False
            p['route_ids'] = False

        newProducts = self.env['product.product'].create(vals)

        for p in newProducts:
            p.product_tmpl_id.generateScancode()
            #routeBuy = p.route_ids.filtered(lambda r: r.id == 7)
            #if len(routeBuy) > 0:
            #    routeBuy[0].unlink()
            routeManu = p.route_ids.filtered(lambda r: r.id == 5)
            if len(routeManu) == 0:
                p.write({'route_ids': [(4, 5)] })# ist der operstortyp für add, die 5 ist die id des co-modells zum ergänzen

        #BOM erzeugen
        newBom = self.env['mrp.bom'].create({
            'code': newProducts[0].default_code,
            'product_id': newProducts[0].id,
            'product_tmpl_id': newProducts[0].product_tmpl_id.id,
            'product_uom_id': newProducts[0].uom_id.id,
            'product_qty' : 1,
            'type' : 'normal',
            'ready_to_produce' : 'asap',
            'company_id' : 1,
            'consumption' : 'warning',
        })
        projectChilds = self.createProjectProductTreeLevel1()

        seq=0
        for p in projectChilds:
            seq+=1
            self.env['mrp.bom.line'].create({
                'product_id': p.id,
                'product_tmpl_id': p.product_tmpl_id.id,
                'product_uom_id': p.uom_id.id,
                'product_qty' : 1,
                'sequence' : seq,
                'bom_id' : newBom.id,
                'company_id' : 1,
            })


    #project erste ebene
    def createProjectProductTreeLevel1(self):

        vals = []
        vals.append({'name': "{}-ohne Zuordnung".format(self.bbi_project_id)})
        vals.append({'name': "{}-Controller".format(self.bbi_project_id)})

        controllersChilds = self.createProjectProductTreeLevel2()

        vals.append({'name': "{}-Kessel".format(self.bbi_project_id)})
        if self.isInSitu:
            vals.append({'name': "{}-Verrohrungsrahmen".format(self.bbi_project_id)})
        vals.append({'name': "{}-Zubehör".format(self.bbi_project_id)})

        for p in vals:
            p['detailed_type'] = "product"
            p['type'] = "product"
            p['purchase_ok'] = False
            p['route_ids'] = False

        newProducts = self.env['product.product'].create(vals)
        for p in newProducts:
            p.product_tmpl_id.generateScancode()
            #routeBuy = p.route_ids.filtered(lambda r: r.id == 7)
            #if len(routeBuy) > 0:
            #    routeBuy[0].unlink()
            routeManu = p.route_ids.filtered(lambda r: r.id == 5)
            if len(routeManu) == 0:
                p.write({'route_ids': [(4, 5)] })# ist der operstortyp für add, die 5 ist die id des co-modells zum ergänzen

        #BOM erzeugen
        newBom = self.env['mrp.bom'].create({
            'code': newProducts[1].default_code,
            'product_id': newProducts[1].id,
            'product_tmpl_id': newProducts[1].product_tmpl_id.id,
            'product_uom_id': newProducts[1].uom_id.id,
            'product_qty' : 1,
            'type' : 'normal',
            'ready_to_produce' : 'asap',
            'company_id' : 1,
            'consumption' : 'warning',
        })

        seq=0
        for p in controllersChilds:
            seq+=1
            self.env['mrp.bom.line'].create({
                'product_id': p.id,
                'product_tmpl_id': p.product_tmpl_id.id,
                'product_uom_id': p.uom_id.id,
                'product_qty' : 1,
                'sequence' : seq,
                'bom_id' : newBom.id,
                'company_id' : 1,
            })

        return newProducts

    #project controller xcubio unterebene
    def createProjectProductTreeLevel2(self):
        vals = []
        vals.append({'name': "{}-Gasmix".format(self.bbi_project_id)})
        vals.append({'name': "{}-ebom".format(self.bbi_project_id)})
        vals.append({'name': "{}-Blendensatz".format(self.bbi_project_id)})
        for p in vals:
            p['detailed_type'] = "product"
            p['type'] = "product"
            p['purchase_ok'] = False
            p['route_ids'] = False

        newProducts = self.env['product.product'].create(vals)

        for p in newProducts:
            p.product_tmpl_id.generateScancode()
            #routeBuy = p.route_ids.filtered(lambda r: r.id == 7)
            #if len(routeBuy) > 0:
            #    routeBuy[0].unlink()
            routeManu = p.route_ids.filtered(lambda r: r.id == 5)
            if len(routeManu) == 0:
                p.write({'route_ids': [(4, 5)] })# ist der operstortyp für add, die 5 ist die id des co-modells zum ergänzen

        return newProducts
