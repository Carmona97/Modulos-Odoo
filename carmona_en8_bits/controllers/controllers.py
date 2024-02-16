# -*- coding: utf-8 -*-
# from odoo import http


# class CarmonaEn8Bits(http.Controller):
#     @http.route('/carmona_en8_bits/carmona_en8_bits', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carmona_en8_bits/carmona_en8_bits/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carmona_en8_bits.listing', {
#             'root': '/carmona_en8_bits/carmona_en8_bits',
#             'objects': http.request.env['carmona_en8_bits.carmona_en8_bits'].search([]),
#         })

#     @http.route('/carmona_en8_bits/carmona_en8_bits/objects/<model("carmona_en8_bits.carmona_en8_bits"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carmona_en8_bits.object', {
#             'object': obj
#         })
