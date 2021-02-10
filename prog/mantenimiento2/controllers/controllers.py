# -*- coding: utf-8 -*-
from odoo import http

# class Mantenimiento2(http.Controller):
#     @http.route('/mantenimiento2/mantenimiento2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mantenimiento2/mantenimiento2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mantenimiento2.listing', {
#             'root': '/mantenimiento2/mantenimiento2',
#             'objects': http.request.env['mantenimiento2.mantenimiento2'].search([]),
#         })

#     @http.route('/mantenimiento2/mantenimiento2/objects/<model("mantenimiento2.mantenimiento2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mantenimiento2.object', {
#             'object': obj
#         })