# -*- coding: utf-8 -*-
{
    'name': "helpdesk_mod",

    'summary': """
        Modificacon al modulo helpeds_mgmt""",

    'description': """
        Modificacon al modulo helpeds_mgmt
    """,

    'author': "Be innovation tech",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'After-Sales',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk_mgmt', 'helpdesk_type', 'maintenance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/helpdesk_mod_security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': False
}
