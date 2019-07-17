		# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InsumosMonopark(models.Model):

	_name = 'insumos.monopark'
	_description = 'Modulo de insumos para monopark'

	producto = fields.Char(string="Producto")
	marca = fields.Char(string="Marca")
	unidad_medida = fields.Char(string="Unidad de medida")
	cantidad = fields.Integer(string="Cantidad")
	proveedor = fields.Many2one('res.partner', string="Proveedor" )
	costo = fields.Float(string="Costo")
