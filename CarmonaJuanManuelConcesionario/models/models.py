# -*- coding: utf-8 -*-

from odoo import models, fields, api


class coche(models.Model):
    _name = 'concesionario.coche'
    _description = 'concesionario.coche'
    _rec_name = 'modelo'

    modelo = fields.Char(string='Modelo')
    fecha = fields.Date(string='año de creacion')
    puertas = fields.Integer(string='cantidad de puertas')
    motor = fields.Selection([('electrico', 'electrico'), ('gasolina', 'gasolina'), ('diesel', 'diesel')], string='Tipo de motor')
    marca = fields.Many2one('concesionario.marca', string='Marca del vehiculo')

class marca(models.Model):
    _name = 'concesionario.marca'
    _description = 'concesionario.marca'
    _rec_name = 'nombre'

    nombre = fields.One2many ('concesionario.coche', 'marca', string='Coche')
    sede = fields.Char(string='Sede')
    director = fields.Char(string='Director')
    direccion = fields.Char(string='Direccion')

class sucursal(models.Model):
    _name = "concesionario.sucursal"
    _description = "concesionario.sucursal"
    _rec_name = "id"

    id = fields.Integer(string='Numero de identificacion de la sucursal')
    localizacion = fields.Char(string='lugar donde se encuentra la sucursal')
    


