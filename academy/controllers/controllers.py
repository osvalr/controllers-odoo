# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': teachers.search([])
        })

    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)
