# -*- coding: utf-8 -*-
{
    'name': "portal2",

    'summary': """
        Portal alternativo para no clientes""",

    'description': """
        Este addon añade un nuevo portal de clientes cuyo proposito es separar modulos que se deban mostrar en un portal pero no en el portal
        de clientes
    """,

    'author': "Be Innovation Tech SAS",
    'website': "https://beitech.com.ar/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance', 'portal', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/portal2.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
