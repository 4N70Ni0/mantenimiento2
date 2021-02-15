# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class mantenimiento_equipo(models.Model):
    _name = 'mantenimiento.equipo'

    nombre = fields.Char(string="Nombre", help="Introduce el nombre del equipo")

    # Trabajador N:M Equipo
    trabajador_ids = fields.Many2many("mantenimiento.trabajador", "trabajador_equipo", "trabajador_id", "equipo_id")
    

class mantenimiento_trabajador(models.Model):
    _name= 'mantenimiento.trabajador'

    dni = fields.Char(string="DNI", help="Introduce el DNI del trabajador", required=True)
    nombre = fields.Char(string="Nombre", help="Introduce el nombre del trabajador", required=True)
    edad = fields.Integer(string="Edad")
    puesto = fields.Char(string="Puesto", required=True)
    Fecha_Contratacion = fields.Date(string="Fecha de contratacion")
    Permisos = fields.Selection([('0', 'Ninguno'),('1', 'Trabajador Equipo'),('2', 'Jefe de Equipo'),('3', 'Jefe de equipos')])
    Telefono = fields.Char(string="Telefono")

    # Trabajador (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "trabajador_id", string="Incidencias", required=True)
    # Trabajador N:M Equipo
    equipo_ids = fields.Many2many("mantenimiento.equipo", "trabajador_equipo", "equipo_id", "trabajador_id")


class mantenimiento_incidencia(models.Model):
    _name= 'mantenimiento.incidencia'

    fecha_y_hora_Inicio = fields.Date(string="Fecha y hora de la incidencia")
    fecha_y_hora_Final = fields.Date(string="Fecha y hora que se marcó el final de la incidencia")
    prioridad = fields.Selection([('0', 'Baja'),('1', 'Moderada'),('2', 'Alta'),('3', 'Peligrosa')])
    descripcion = fields.Char(string="Descripcion", help="Introduce una descripción")
    # Procesando es el valor por defecto, en cuanto el jefe de equipo acepte la incidencia, pasará a 'En proceso'.
    estado = fields.Selection([('0', 'Procesando...'),('1', 'En proceso'),('2', 'Completado'),('3', 'Cancelado')], default=0)

    # Trabajador 1:(N) Incidencia
    trabajador_id = fields.Many2one("mantenimiento.trabajador", string="Trabajador")
    # Tipo de incidencia 1:(N) Incidencia
    tipo_id = fields.Many2one("mantenimiento.tipo", string="Tipo de incidencia", required=True)

    # Campo calculado
    duracion_incidencia = fields.Integer(string="Duración de la incidencia (días)", compute="_duracion", store=True)

    @api.depends("fecha_y_hora_Inicio", "fecha_y_hora_Final")
    def _duracion(self):
        for r in self:
            # Calcular la diferencia de tiempo
            r.duracion_incidencia = (r.fecha_y_hora_Final - r.fecha_y_hora_Inicio).days


class mantenimiento_tipo(models.Model):
    _name='mantenimiento.tipo'

    nombre = fields.Char(string="Tipo", required=True, help="Tipo de incidencia")

    # Tipo de incidencia (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "tipo_id", string="Incidencias", required=True)

