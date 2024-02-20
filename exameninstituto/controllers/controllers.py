# -*- coding: utf-8 -*-
# from odoo import http


# class Exameninstituto(http.Controller):
#     @http.route('/exameninstituto/exameninstituto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exameninstituto/exameninstituto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('exameninstituto.listing', {
#             'root': '/exameninstituto/exameninstituto',
#             'objects': http.request.env['exameninstituto.exameninstituto'].search([]),
#         })

#     @http.route('/exameninstituto/exameninstituto/objects/<model("exameninstituto.exameninstituto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exameninstituto.object', {
#             'object': obj
#         })
