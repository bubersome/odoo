# -*- coding: utf-8 -*-
# from odoo import http


# class RexMail(http.Controller):
#     @http.route('/rex_mail/rex_mail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rex_mail/rex_mail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rex_mail.listing', {
#             'root': '/rex_mail/rex_mail',
#             'objects': http.request.env['rex_mail.rex_mail'].search([]),
#         })

#     @http.route('/rex_mail/rex_mail/objects/<model("rex_mail.rex_mail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rex_mail.object', {
#             'object': obj
#         })
