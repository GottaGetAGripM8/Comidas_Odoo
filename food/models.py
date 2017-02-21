# -*- coding: utf-8 -*-

from openerp import models, fields, api

#class Platos(models.Model): 
    

#class Decoracion(models.Model): 


class Camareros(models.Model): 
	_name = 'food.camareros'
	name = fields.Char(string="Nombre Camarero", required=True)
	camareros_id = fields.One2Many('food.mesas', 'mesas_id', string="Mesa")

class Mesas(models.Model): # 1 MESA solo la lleva un CAMARERO
	_name = 'food.mesas'
	name = fields.Char(string="Nombre Mesa", required=True)
	mesas_id = fields.Many2One('food.camareros', string="Camareros")
	    
