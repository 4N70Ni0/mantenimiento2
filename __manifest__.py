# -*- coding: utf-8 -*-
{
    'name': "Mantenimiento 2",

    'summary': """
        Proyecto para la asignatura de SGES""",

    'description': """
       Modulo creado por Antonio Bañon y Sergio Orellana para la asignatura SGES sobre mantenimiento de equipamiento 
    """,

    'author': "My Company",
    'website': "http://www.yourcomny.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'application': True,
    'installable': True,
}
