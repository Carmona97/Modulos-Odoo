# -*- coding: utf-8 -*-

import re
from jsonschema import ValidationError
from odoo import models, fields, api


class usuarios(models.Model):
    _name = 'carmona_en8_bits.usuarios'
    _description = 'carmona_en8_bits.usuarios'
    _rec_name = "nombre"
     
    dni = fields.Text(string="dni del usuario", size=9,help="dni completo",required=True)
    nombre = fields.Text(string="nombre del usuario",help="introduzca su nombre",required=True)
    apellidos = fields.Text(string="apellidos del usuario",help="introduzca su apellido",required=True)
    fechaNacimiento = fields.Date(string="fecha de nacimiento del usuario",help="indique su fecha de nacimiento")

    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if record.dni:
                # Verificar que el DNI tenga exactamente 9 caracteres
                if len(record.dni) != 9:
                    raise ValidationError("El DNI debe tener 9 caracteres")

                
class cuentas(models.Model):
    _name = 'carmona_en8_bits.cuentas'
    _description = 'carmona_en8_bits.cuentas'
    _rec_name = "nombreCuenta"

    idCuenta = fields.Integer() 
    nombreCuenta = fields.Text(string="nombre de la cuenta asociada al usuario")
    contrasena = fields.Text(string="contraseña de la cuenta")
    personajesCuenta = fields.One2many("carmona_en8_bits.personajes","cuenta", string="Personajes de la cuenta")
    usuario = fields.Many2one('carmona_en8_bits.usuarios', string="Usuario dueño de la cuenta")
    

class personajes(models.Model):
    _name = 'carmona_en8_bits.personajes'
    _description = 'carmona_en8_bits.personajes'
    _rec_name = "nombrePersonaje"

    idPersonaje = fields.Integer()
    nombrePersonaje = fields.Text(string="Nombre del personaje")
    cuenta = fields.Many2one("carmona_en8_bits.cuentas")
    objetos = fields.Many2many("carmona_en8_bits.objetos")
    misiones = fields.Many2many("carmona_en8_bits.misiones")
    clase = fields.Selection([('Guerrero', 'Guerrero'), ('Mago', 'Mago'), ('Clerigo', 'Clerigo'), ('Picaro', 'Picaro'), ('Druida', 'Druida'), ('Bardo', 'Bardo'), ('Brujo', 'Brujo')], string='Clase del personaje')
    nivel = fields.Integer(string="Nivel",size = 100)
    raza = fields.Selection([('Elfo', 'Elfo'), ('Humano', 'Humano'), ('Enano', 'Enano'), ('Mediano', 'Mediano'), ('Gnomo', 'Gnomo'), ('Trasgo', 'Trasgo'), ('Orco', 'Orco')], string='Raza del personaje') 
    HP = fields.Integer(string="Puntos de vida", readonly=True)
    ATK = fields.Integer(string="Puntos de ataque", readonly=True)
    DEF = fields.Integer(string="Puntos de defensa", readonly=True)

    @api.onchange('clase', 'nivel')
    def _compute_stats(self):
        for record in self:
            if record.clase in ['Mago', 'Picaro', 'Brujo', 'Druida']:
                record.ATK = record.nivel * 7
                record.DEF = record.nivel * 3
                record.HP = record.nivel * 120
            else:
                record.ATK = record.nivel * 2
                record.DEF = record.nivel * 8
                record.HP = record.nivel * 165

class objetos(models.Model):
    _name = 'carmona_en8_bits.objetos'
    _description = 'carmona_en8_bits.objetos'
    _rec_name = "nombreObjeto"

    idObjeto = fields.Integer()
    nombreObjeto = fields.Text(string="Nombre del objeto")
    objetosPersonajes =  fields.Many2many("carmona_en8_bits.personajes")
    descripcion = fields.Text("Para que sirve el objeto")
    imagenObjeto = fields.Binary(string="Imagen del objeto")
    tipo = fields.Selection([('Consumible', 'Consumible'), ('Equipo', 'Equipo'), ('Artefacto', 'Artefacto')])
    precio = fields.Float("Valor del mercado del objeto")
    intercambiable = fields.Boolean("Indica si el objeto puede ser traspasado a otro jugador")

class misiones(models.Model):
    _name = 'carmona_en8_bits.misiones'
    _description = 'carmona_en8_bits.misiones'
    _rec_name = "nombreMision"

    idMision = fields.Integer()
    nombreMision = fields.Text(string="Nombre de la mision")
    misionPersonajes = fields.Many2many("carmona_en8_bits.personajes")
    region = fields.Many2one("carmona_en8_bits.regiones")
    descripcion = fields.Text(string="Indica el objetivo de la mision")
    recompensas = fields.Text(string="Recompensa de la mision")
    estado = fields.Selection([('Pendiente', 'Pendiente'), ('En curso', 'En curso'), ('Completada', 'Completada')])

class regiones(models.Model):
    _name = 'carmona_en8_bits.regiones'
    _description = 'carmona_en8_bits.regiones'
    _rec_name = "nombreRegion"

    nombreRegion = fields.Selection([("Northel", "Northel"),("Surthal", "Surthal"),("Esthil", "Esthil"),("Oesthul", "Oesthul"),("Capithol", "Capithol")])
    clima = fields.Text(string="Clima habitual de la region")
    cantidadMazmorras = fields.Integer(string="cantidad de mazmorras de la region")
    misiones = fields.One2many("carmona_en8_bits.misiones","region")
