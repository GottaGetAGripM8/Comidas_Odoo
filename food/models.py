# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Platos(models.Model): 
	_name = 'food.platos'

	name = fields.Char(string="Nombre del Plato", required=True)

	#camareros_id = fields.Many2many(string="Camareros", comodel_name='zoo.camareros', relation='rel_camarero_plato', column1='plato', column2='camarero')
	#veterinarios_id=fields.Many2many(string="Veterinarios", comodel_name='zoo.veterinario', relation='rel_veterinario_animal', column1='animal', column2='veterinario')s

#class Decoracion(models.Model): #1 decoracion puede estar en N varias mesas
	#_name = 'food.decoracion'

	#name = fields.Char(string="Nombre de la decoracion", required=True)

	#decoracion_id = fields.One2many('food.decoracion', 'mesas_id', string="Decoracion")


class Camareros(models.Model): 
	_name = 'food.camareros'

	name = fields.Char(string="Nombre del camarero", required=True)
	sexo = fields.Selection([('mujer','Mujer'), ('hombre','Hombre')], 'sexo')

	mesas_id = fields.One2many('food.camareros', 'mesas_id', string="Mesa")
	platos_id = fields.Many2many(string="Platos", comodel_name='food.platos', relation='rel_plato_camareros', column1='camareros', column2='plato')
	#animales_id=fields.Many2many(string="Animales", comodel_name='zoo.animal', relation='rel_animal_veterinario', column1='veterinario', column2='animal')
	
class Mesas(models.Model): # 1 MESA solo la lleva un CAMARERO
	_name = 'food.mesas'

	name = fields.Char(string="Nombre de la mesa", required=True)

	camareros_id = fields.Many2one('food.mesas', string="Camareros")
	decoracion_id = fields.Many2one('food.mesas', string="Decoracion")



	    
