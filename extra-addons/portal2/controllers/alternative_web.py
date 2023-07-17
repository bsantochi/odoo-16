# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.portal.controllers import web
from odoo.http import request


class Home(web.Home):

    @http.route()
    def index(self, *args, **kw):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('portal2.group_maintenance_portal2'):
            return request.redirect_query('/my_portal_2', query=request.params)
        return super(Home, self).index(*args, **kw)

    def _login_redirect(self, uid, redirect=None):
        if not redirect and request.env['res.users'].sudo().browse(uid).has_group('portal2.group_maintenance_portal2'):
            redirect = '/my_portal_2'
        return super(Home, self)._login_redirect(uid, redirect=redirect)

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('portal2.group_maintenance_portal2'):
            return request.redirect_query('/my_portal_2', query=request.params)
        return super(Home, self).web_client(s_action, **kw)