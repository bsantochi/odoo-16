# -*- coding: utf-8 -*-
{
    'name': "maintenance_betech",

    'summary': """
        Maintenance Portal para Be Tech """,

    'description': """
        Modificaciones del addon "maintenance_portal" para Venturi
    """,

    'author': "Be Innovation Tech SAS",
    'website': "https://beitech.com.ar/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance_portal', 'stock'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
