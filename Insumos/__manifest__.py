# -*- coding: utf-8 -*-
{
    'name': "insumos",

    'summary': """       
        Module for the registration of inputs of the company.""",

    'description': """
        Module for the registration of inputs of the company.
    """,

    'author': "Xmarts",
    'Collaborators': "Gilberto Santiago Acevedo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}