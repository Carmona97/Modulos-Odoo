# -*- coding: utf-8 -*-

from odoo import models, fields, api



class profesor(models.Model):
    _name = 'exameninstituto.profesor'
    _description = 'exameninstituto.profesor'
    _rec_name = "nombreProfesor"

    nombreProfesor = fields.Text(string="Nombre del profesor")
    direccion = fields.Text()
    ciudad = fields.Selection([('malaga', 'malaga'), ('sevilla', 'sevilla'), ('cadiz', 'cadiz'), ('granada', 'granada'), ('cordoba', 'cordoba'), ('huelva', 'huelva'), ('almeria', 'almeria')])
    telefono = fields.Text()
    asignaturas = fields.One2many("exameninstituto.asignatura","profesor")

class estudiante(models.Model):
    _name = 'exameninstituto.estudiante'
    _description = 'exameninstituto.estudiante'
    _rec_name = "nombreEstudiante"

    nombreEstudiante = fields.Text(string="Nombre del estudiante")
    apellidos = fields.Text()
    direccion = fields.Text()
    ciudad = fields.Selection([('malaga', 'malaga'), ('sevilla', 'sevilla'), ('cadiz', 'cadiz'), ('granada', 'granada'), ('cordoba', 'cordoba'), ('huelva', 'huelva'), ('almeria', 'almeria')])
    asignaturas = fields.Many2many("exameninstituto.asignatura")

class asignatura(models.Model):
    _name = 'exameninstituto.asignatura'
    _description = 'exameninstituto.asignatura'
    _rec_name = "nombreAsignatura"

    nombreAsignatura = fields.Text(string="Nombre de la asignatura")
    nivel = fields.Text()
    imagen = fields.Binary(string="Imagen de la asignatura")
    profesor = fields.Many2one("exameninstituto.profesor")
    alumnado = fields.Many2many("exameninstituto.estudiante")