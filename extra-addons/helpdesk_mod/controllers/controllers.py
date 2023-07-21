import base64
import werkzeug

from odoo import http
from odoo.http import request

from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

class HelpdeskModTicketController(HelpdeskTicketController):
    @http.route("/new/ticket", type="http", auth="user", website=True)
    def create_new_ticket(self, **kw):
        ticket_type = http.request.env["helpdesk.ticket.type"].search([])
        email = http.request.env.user.email
        name = http.request.env.user.name
        helpdesk_team = http.request.env["helpdesk.ticket.team"].search([])
        return http.request.render(
            "helpdesk_mgmt.portal_create_ticket",
            {"type": ticket_type, "email": email, "name": name, "helpdesk_team":helpdesk_team},
        )

    @http.route("/submitted/ticket", type="http", auth="user", website=True, csrf=True)
    def submit_ticket(self, **kw):
        vals = {
            "company_id": http.request.env.user.company_id.id,
            "type_id": kw.get("tipo"),
            "description": kw.get("description"),
            "name": kw.get("subject"),
            "attachment_ids": False,
            "channel_id": request.env["helpdesk.ticket.channel"]
            .sudo()
            .search([("name", "=", "Web")])
            .id,
            "partner_id": request.env.user.partner_id.id,
            "partner_name": request.env.user.partner_id.name,
            "partner_email": request.env.user.partner_id.email,
            "team_id": kw.get("team")
        }
        new_ticket = request.env["helpdesk.ticket"].sudo().create(vals)
        new_ticket.message_subscribe(partner_ids=request.env.user.partner_id.ids)
        if kw.get("attachment"):
            for c_file in request.httprequest.files.getlist("attachment"):
                data = c_file.read()
                if c_file.filename:
                    request.env["ir.attachment"].sudo().create(
                        {
                            "name": c_file.filename,
                            "datas": base64.b64encode(data),
                            "res_model": "helpdesk.ticket",
                            "res_id": new_ticket.id,
                        }
                    )
        return werkzeug.utils.redirect("/my/tickets")