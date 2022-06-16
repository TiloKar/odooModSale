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
     - sale order als CSV auslesbar, Juni 22
    """,
  'depends': [
    'base',
    'sale',
    'product',
    'stock',
    'resource',
  ],
  'data': [
    'report/bbi_report_saleorder_document.xml',
    'report/bbi_report_saleorder.xml',
    'report/bbi_report_proforma.xml',
    'views/bbi_csv_webshop.xml',
  ],
}
