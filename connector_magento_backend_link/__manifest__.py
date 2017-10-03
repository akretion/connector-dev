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
    'name': 'Connector Magento Backend Link',
    'version': '0.2',
    'author': 'Akretion',
    'maintainer': 'Akretion',
    'category': 'Connector',
    'depends': [
        'connector_base_backend_link',
    ],
    'description': """
Connector Magento Backend Link
====================================

Description
---------------
This module provide magento models mapping with openerp to display
url to magento backend

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
    'installable': False,
    'license': 'AGPL-3',
    'auto_install': False,
    'application': False,
}
