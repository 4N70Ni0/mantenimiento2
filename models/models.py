# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mantenimiento_equipo(models.Model):
    _name = 'mantenimiento.equipo'

    nombre = fields.Char(string="Nombre", help="Introduce el nombre del equipo")

    # Trabajador N:M Equipo
    trabajador_ids = fields.Many2many("mantenimiento.trabajador", "trabajador_equipo", "trabajador_id", "equipo_id")


class mantenimiento_incidencia(models.Model):
    _name= 'mantenimiento.incidencia'

    fecha_y_hora_Inicio = fields.Date(string="Fecha y hora de la incidencia")
    fecha_y_hora_Final = fields.Date(string="Fecha y hora que se marcó el final de la incidencia")
    #destinatario = fields.One2many('mantenimiento.equipo', string="Trabajador")#Enterate bien de como se poner relaciones
    prioridad = fields.Integer(string="Prioridad", help="Introduce la prioridad de la incidencia")
    #tipo_de_incidencia = fields.Many2one('mantenimiento.tipo', string="Tipo de incidencia")
    descripcion = fields.Char(string="descripcion", help="Introduce una descripción")
    estado = fields.Integer(string="estado")

    # Trabajador 1:(N) Incidencia
    trabajador_id = fields.Many2one("mantenimiento.trabajador", string="Trabajador", required=True)
    # Tipo de incidencia 1:(N) Incidencia
    tipo_id = fields.Many2one("mantenimiento.tipo", string="Tipo de incidencia", required=True)
    

class mantenimiento_trabajador(models.Model):
    _name= 'mantenimiento.trabajador'

    dni = fields.Char(string="DNI", required=True, help="Introduce el DNI del trabajador")
    nombre = fields.Char(string="Nombre", required=True, help="Introduce el nombre del trabajador")
    edad = fields.Integer(string="edad")
    puesto = fields.Char(string="Puesto")
    Fecha_Contratacion = fields.Date(string="fecha de contratacion")
    Permisos = fields.Integer(string="permisos")
    Telefono = fields.Char(string="Telefono")
    #equipo = fieldsMany2many('mantenimiento.equipo', string="Equipo al que pertenece el trabajador")

    # Trabajador (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "trabajador_id", string="Incidencias", required=True)
    # Trabajador N:M Equipo
    equipo_ids = fields.Many2many("mantenimiento.equipo", "trabajador_equipo", "equipo_id", "trabajador_id")


class mantenimiento_tipo(models.Model):
    _name='mantenimiento.tipo'

    nombre = fields.Char(string="Tipo", required=True, help="tipo de incidencia")

    # Tipo de incidencia (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "tipo_id", string="Incidencias", required=True)

