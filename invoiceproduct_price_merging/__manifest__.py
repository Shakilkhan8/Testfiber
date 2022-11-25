# -*- coding: utf-8 -*-
{
    'name': "Invoice Product Price Merging",

    'summary': """This module is all about invoice line product pricing""",

    'description': """
        This module is used to give same price for all those product 
        on one click which has same category and quality
    """,

    'author': "SK Technology",

    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account_accountant'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
