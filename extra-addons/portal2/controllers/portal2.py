from odoo import _, http
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request
import werkzeug

class Portal2(CustomerPortal):

    # def _prepare_home_portal_values(self, counters):
    #     return super()._prepare_home_portal_values(counters)

    # @http.route(['/my_portal_2/counters'], type='json', auth="user", website=True)
    # def portal2_counters(self, counters, **kw):
    #     return self._prepare_home_portal_values(counters)
    # @http.route(['/my_portal_2/counters'], type='json', auth="user", website=True)
    # def portal2_counters(self, counters, **kw):
    #     return super()._prepare_home_portal_values(counters)
    
    @http.route(['/my_portal_2', '/my_portal_2/home'], type='http', auth="user", website=True)
    def portal2_home(self, **kw):
        values = super()._prepare_portal_layout_values()
        return request.render("portal2.portal2_my_home", values)


    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        if request.env['res.users'].sudo().browse(request.session.uid).has_group('portal2.group_maintenance_portal2'):
            return request.redirect_query('/my_portal_2/home', query=request.params)
            # return self.portal2_home(**kw)
        return super(Portal2, self).home(**kw)
