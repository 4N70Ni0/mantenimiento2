# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class mantenimiento_equipo(models.Model):
    _name = 'mantenimiento.equipo'

    nombre = fields.Char(string="Nombre", 
            help="Nombre del equipo", required=True)

    # Trabajador N:M Equipo
    trabajador_ids = fields.Many2many("mantenimiento.trabajador", "trabajador_equipo", "trabajador_id", "equipo_id", 
            help="Añadir trabajadores al equipo")
    

class mantenimiento_trabajador(models.Model):
    _name= 'mantenimiento.trabajador'

    dni = fields.Char(string="DNI", 
            help="DNI del trabajador", required=True)
    nombre = fields.Char(string="Nombre", 
            help="Nombre del trabajador", required=True)
    edad = fields.Integer(string="Edad", 
            help="Edad del trabajador")
    puesto = fields.Char(string="Puesto", 
            help="Puesto del trabajador", required=True)
    Fecha_Contratacion = fields.Date(string="Fecha de contratacion", 
            help="Fecha de contratación del trabajador")
    Permisos = fields.Selection([('0', 'Ninguno'),('1', 'Trabajador Equipo'),('2', 'Jefe de Equipo'),('3', 'Jefe de equipos')], 
            help="Permisos del trabajador en el equipo")
    Telefono = fields.Char(string="Telefono", 
            help="Número telefónico del trabajador")

    # Trabajador (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "trabajador_id", string="Incidencias", 
            help="Incidencias reportadas por el trabajador", required=True)
    # Trabajador N:M Equipo
    equipo_ids = fields.Many2many("mantenimiento.equipo", "trabajador_equipo", "equipo_id", "trabajador_id", 
            help="Equipos a los que pertenece el trabajador")


class mantenimiento_incidencia(models.Model):
    _name= 'mantenimiento.incidencia'

    descripcion = fields.Char(string="Descripción", 
            help="Descripción de la incidencia", required=True)
    estado = fields.Selection([('0', 'Procesando...'),('1', 'En proceso'),('2', 'Completado'),('3', 'Cancelado')], default='0', 
            help="Estado en el que se encuentra la incidencia", required=True)
    fecha_Inicio = fields.Date(string="Inicio de la incidencia", 
            help="Fecha de inicio de la incidencia", required=True)
    fecha_Final = fields.Date(string="Solventación de la incidencia", 
            help="Fecha de finalización de la incidencia")
    prioridad = fields.Selection([('0', 'Baja'),('1', 'Moderada'),('2', 'Alta'), ('3', 'Muy alta')], 
            help="Prioridad de la incidencia")
    # Procesando es el valor por defecto, en cuanto el jefe de equipo acepte la incidencia, pasará a 'En proceso'.

    # Trabajador 1:(N) Incidencia
    trabajador_id = fields.Many2one("mantenimiento.trabajador", string="Trabajador", 
            help="Seleccione al trabajador que reportó la incidencia")
    # Tipo de incidencia 1:(N) Incidencia
    tipo_id = fields.Many2one("mantenimiento.tipo", string="Tipo de incidencia", 
            help="Tipo de la incidencia", required=True)

    # Campo calculado
    duracion_incidencia = fields.Integer(string="Duración de la incidencia (días)", compute="_duracion", store=True, 
            help="Tiempo transcurrido desde que se reportó la incidencia hasta que se subsanó el problema")

    @api.depends("fecha_Inicio", "fecha_Final")
    def _duracion(self):
        for r in self:
            # Calcular la diferencia de tiempo
            try:
                r.duracion_incidencia = (r.fecha_Final - r.fecha_Inicio).days
            except TypeError as ex:
                r.duracion_incidencia = 0

class mantenimiento_tipo(models.Model):
    _name='mantenimiento.tipo'

    nombre = fields.Char(string="Tipo", 
            help="Añada un tipo de incidencia", required=True)

    # Tipo de incidencia (1):N Incidencia
    incidencias_ids = fields.One2many("mantenimiento.incidencia", "tipo_id", string="Incidencias", 
            help="Incidencias pertenecientes a este tipo", required=True)

