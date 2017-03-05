# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Platos(models.Model): 
	_name = 'food.platos'

	name = fields.Char(string="Nombre del Plato", required=True)
	tipo = fields.Selection([('primer_plato','Primer Plato'), ('segundo_plato','Segundo Plato'), ('postre','Postre')], 'tipo_de_plato')

	camareros_id = fields.Many2many(string="Camareros", comodel_name='food.camareros', relation='rel_camarero_plato', column1='plato', column2='camarero')

class Decoracion(models.Model): 
	_name = 'food.decoracion'

	name = fields.Char(string="Nombre de la decoracion", required=True)
	tipo = fields.Selection([('invernal','Festival de Invernal'), ('halloween','Festival de Halloween'), ('primavera','Festival de la Primavera')], 'decoracion_festival')

	mesas_id = fields.One2many('food.mesas', 'decoracion_id', string="Decoracion")

class Camareros(models.Model): 
	_name = 'food.camareros'

	name = fields.Char(string="Nombre del camarero", required=True)
	sexo = fields.Selection([('mujer','Mujer'), ('hombre','Hombre')], 'sexo')
	edad = fields.Integer(string="Edad ", required=True)

	mesas_id = fields.One2many('food.mesas', 'camareros_id', string="Mesa")
	platos_id = fields.Many2many(string="Platos", comodel_name='food.platos', relation='rel_plato_camareros', column1='camareros', column2='plato')
	
	
class Mesas(models.Model):
	_name = 'food.mesas'

	name = fields.Char(string="Nombre de la mesa", required=True)

	camareros_id = fields.Many2one('food.camareros', string="Camareros")
	decoracion_id = fields.Many2one('food.decoracion', string="Decoracion")



	    
