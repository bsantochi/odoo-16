# -*- coding: utf-8 -*-
{
    'name': "maintenance_venturi",

    'summary': """
        Maintenance Portal para Venturi""",

    'description': """
        Modificaciones del addon "maintenance_portal" para Venturi
    """,

    'author': "Be Innovation Tech SAS",
    'website': "https://beitech.com.ar/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance_portal', 'stock', 'helpdesk_mgmt'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
