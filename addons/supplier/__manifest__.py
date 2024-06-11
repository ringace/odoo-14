# -*- coding: utf-8 -*-
{
    'name': "Supplier Module",

    'summary': """Register Supplier""",

    'description': """
        Register supplier as a master supplier
    """,

    'author': "Doring Manuwian",
    'website': "",

    'category': 'Manufacturing',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/supplier_view.xml',
        'views/supplier_action.xml',
        'views/supplier_menuitem.xml',
    ],

    'installable': True,
    'application': True,
}