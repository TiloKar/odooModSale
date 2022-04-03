# -*- coding: utf-8 -*-
# bbi Customisation für Freitextnotizen in Angebotspositionen
# @author: Tilo K
# @date:    April 2022
# Version 1.0 Webshopeigenschaft an product_template, Positionsfreitext im angebot vom Produkt

{
  'name': 'bbi mod sale',
  'version': '1.0',
  'category': 'Sale',
  'description': """
     - verkürzte Übernahme der Sale-Produktbeschreibung in Angebotspositionen
     - Erweiterung Produkt um Webshopeigenschaft
    """,
  'depends': [
    'base',
    'sale',
    'product',
    'stock',
    'resource',
  ],
  'data': [
    'views/product_template_form_view_bbi.xml',
    'views/product_template_tree_view_bbi.xml',
  ],
}
