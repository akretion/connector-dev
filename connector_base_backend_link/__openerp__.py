# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: David BEAL
#    Copyright 2013 Akretion SARL
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Connector Base Backend Link',
    'version': '0.2',
    'author': 'Akretion',
    'maintainer': 'Akretion',
    'category': 'Connector',
    'depends': [
        'connector_ecommerce',
    ],
    'description': """
Connector Base Backend Link
===============================

Description
---------------
This module allows to define contextual url link towards external backend
like magento or any application connected to openerp using connector

For now fields are defined in these models and can be used in views:
- 'sale.order'
- 'queue.job'

Requirements
---------------
This 


Installation
--------------
Display and populate in your backend view, the 'url_external_backend' field
with debugger mode or a custom module


Contributors
-----------------
* David BEAL <david.beal@akretion.com>

----

*TODO*:

    - add link to other objects

    """,
    'website': 'http://www.akretion.com/',
    'data': [
        'model_view.xml',
    ],
    'tests': [],
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,
    'application': False,
}
