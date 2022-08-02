# -*- coding: utf-8 -*-
# bbi Customisation für Freitextnotizen in Angebotspositionen
# @author: Tilo K
# @date:    April 2022
# Version 1.0 Webshopeigenschaft an product_template, Positionsfreitext im angebot vom Produkt

{
  'name': 'bbi_mod_sale',
  'version': '1.3',
  'author': "Hanning Liu, Tilo Karczewski",
  'category': 'Sale',
  'description': """
     - verkürzte Übernahme der Sale-Produktbeschreibung in Angebotspositionen, März 22
     - Erweiterung Produkt um Webshopeigenschaft, umgezogen in bbi_mod_stock in Mai 22
     - qweb report hacks in mod integriert, Juni 22
    """,
  'depends': [
    'base',
    'sale',
    'product',
    'stock',
    'resource',
  ],
  'data': [
    'report/bbi_external_layout.xml',
    'report/bbi_report_saleorder.xml',
    'report/bbi_report_proforma.xml',
    'report/paperformat_bbi.xml',
    'report/minified_saleorder.xml',
    'report/change_paperformat.xml',
    'data/sequense_saleorder_to_bzv.xml',
    'views/sale_order_form_bbi.xml',
    'security/fundamental_groups.xml',
    'security/ir.model.access.csv',
    'security/bbi_sale_security.xml',
  ],
}
