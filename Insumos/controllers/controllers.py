# -*- coding: utf-8 -*-
from odoo import http

# class InsumosMono(http.Controller):
#     @http.route('/insumos_mono/insumos_mono/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/insumos_mono/insumos_mono/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('insumos_mono.listing', {
#             'root': '/insumos_mono/insumos_mono',
#             'objects': http.request.env['insumos_mono.insumos_mono'].search([]),
#         })

#     @http.route('/insumos_mono/insumos_mono/objects/<model("insumos_mono.insumos_mono"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('insumos_mono.object', {
#             'object': obj
#         })