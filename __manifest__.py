# -*- coding: utf-8 -*-
# bbi Customisation für Freitextnotizen in Angebotspositionen
# @author: Tilo K
# @date:    April 2022
# Version 1.0 Webshopeigenschaft an product_template, Positionsfreitext im angebot vom Produkt

{
  'name': 'bbi_mod_sale',
  'version': '1.2',
  'author': "Hanning Liu, Tilo Karczewski",
  'category': 'Sale',
  'description': """
     - verkürzte Übernahme der Sale-Produktbeschreibung in Angebotspositionen, März 22
     - Erweiterung Produkt um Webshopeigenschaft, umgezogen in bbi_mod_stock in Mai 22
     - TODO Idee Blendenmanagement, Lochbild als Produkt (eigene Kategorie Lochbild
     mit hoher ID, eigene Kategorie Blende mit hoher ID ), Stückliste mit Rohling-Blende
     und Lochbildern als BOM, rekursive Prüfung bei BOM.create() in dieser Kategorie, ob eine vergleichbare BOM schon existiert!
     - TODO bbi Lagerort als Attribut ...bbi_location_id = fields.Many2one... mit eigener Lagerortentität
     - TODO Eigenschaft Ersatzteil für Ersatzteil-Stücklisten Generator (bool)
    """,
  'depends': [
    'base',
    'sale',
    'product',
    'stock',
    'resource',
  ],
  'data': [
  ],
}
