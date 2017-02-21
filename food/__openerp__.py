# -*- coding: utf-8 -*-
{
    'name': "Comidas",

    'summary': """Comidas""",
    
    'description': """Modulo de Comidas""",


    'author': "Andreea Birsan, Mayuri Budria, Alberto Elcoso y Javier Pardos",
    'website': "SALESIANOS.EDU",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'modulo final',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
