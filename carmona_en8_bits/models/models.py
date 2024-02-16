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
                
                # Verificar que el DNI contenga solo números
                if not record.dni.isdigit():
                    raise ValidationError("El DNI solo puede contener números")
                
                # Verificar el formato del DNI
                dni_pattern = r'^[0-9]{8}[A-Za-z]$'
                if not re.match(dni_pattern, record.dni):
                    raise ValidationError("Formato de DNI no válido")
                
                # Verificar la letra del DNI
                letra = record.dni[-1].upper()
                letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
                dni_numeros = int(record.dni[:-1])
                if letra != letras_validas[dni_numeros % 23]:
                    raise ValidationError("Letra del DNI incorrecta")
                
class cuentas(models.Model):
    _name = 'carmona_en8_bits.cuentas'
    _description = 'carmona_en8_bits.cuentas'
    _rec_name = "nombreCuenta"

    idCuenta = fields.Integer() 
    nombreCuenta = fields.Text(string="nombre de la cuenta asociada al usuario")
    contrasena = fields.Text(string="contraseña de la cuenta")
    personajesCuenta = fields.One2many("carmona_en8_bits.personajes","cuenta")

class personajes(models.Model):
    _name = 'carmona_en8_bits.personajes'
    _description = 'carmona_en8_bits.personajes'
    _rec_name = "nombrePersonaje"

    idPersonaje = fields.Integer()
    nombrePersonaje = fields.Text(string="Nombre del personaje")
    cuenta = fields.Many2one("carmona_en8_bits.cuentas")
    objetos = fields.Many2many("carmona_en8_bits.objetos")
    misiones = fields.Many2many("carmona_en8_bits.misiones")
    clase = fields.Selection([('Guerrero', 'Guerrero'), ('Mago', 'gasolina'), ('Picaro', 'diesel'), ('Picaro', 'diesel'), ('Picaro', 'diesel'), ('Picaro', 'diesel'), ('Picaro', 'diesel')], string='Tipo de motor')("Guerrero","Mago","Clerigo","Picaro","Druida","Bardo","Brujo")
    nivel = fields.Integer(string="Nivel",size = 100)
    raza = fields.enum("Elfo","Humano","Enano","Mediano","Gnomo","Trasgo","Orco","Drow")
    HP = fields.Integer(string="Puntos de vida", readonly=True)
    ATK = fields.Integer(string="Puntos de ataque", readonly=True)
    DEF = fields.Integer(string="Puntos de defensa", readonly=True)

    @api.onchange('clase', 'nivel')
    def _compute_stats(self):
        for record in self:
            if record.clase in ['mago', 'picaro', 'brujo', 'druida']:
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
    tipo = fields.enum("Consumible","Equipo","Artefacto")
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
    estado = fields.enum("Pendiente","Completada")

class regiones(models.Model):
    _name = 'carmona_en8_bits.regiones'
    _description = 'carmona_en8_bits.regiones'
    _rec_name = "nombreRegion"

    nombreRegion = fields.enum("Northel","Surthal","Esthil","Oesthul","Capithol")
    clima = fields.enum("Sol","Lluvia","Nieve")
    cantidadMazmorras = fields.Integer(string="cantidad de mazmorras de la region")
    misiones = fields.One2many("carmona_en8_bits.misiones","region")
