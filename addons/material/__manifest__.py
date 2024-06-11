# -*- coding: utf-8 -*-
{
    'name': "Material Module",

    'summary': """Register Material""",

    'description': """
        Register material by supplier name
    """,

    'author': "Doring Manuwian",
    'website': "",

    'category': 'Manufacturing',
    'version': '0.1',

    'depends': ['base', 'supplier'],

    'data': [
        'security/ir.model.access.csv',
        'views/material_view.xml',
        'views/material_action.xml',
        'views/material_menuitem.xml',
    ],

    'installable': True,
    'application': True,
}