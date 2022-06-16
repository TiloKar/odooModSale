from odoo import api, fields, models, _
import csv, base64, sys, xlrd, io
from odoo.exceptions import ValidationError
import os

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    csvdata = fields.Binary(String='CSV File')
    csvdata_file_name = fields.Char(String='Name')

    def csv_auslesen(self):

        temp = 0
        listoflists = []
        message = ''
        for i in self:
            for j in i.order_line:
                message = message + str(j.product_uom_qty) + ';' + str(j.product_id.default_code)  + ';' + 'Test' + '\n'
                #templist = [j.product_uom_qty, j.product_id.default_code, 'Test']
                #listoflists.append(templist)
                #temp = temp + 1
        #raise ValidationError (str(listoflists))


        raw = str(message).encode(encoding='utf-8', errors='replace')
        self.csvdata = base64.b64encode(raw)

        self.csvdata_file_name = 'CSV Datei.csv'
