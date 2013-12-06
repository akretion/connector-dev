# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Sébastien BEAU
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

{'name': 'Connector dev',
 'version': '7.0.1',
 'author': 'Openerp Connector Core Editors',
 'website': 'https://launchpad.net/openerp-connector',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
.Helper to connector to retry instantly to perform a job.
It add a button in backend to retry failed job.
""",
 'depends': ['connector',
             'cron_run_manually',
             'magentoerpconnect',
             ],
 'data': ['job_view.xml',
          ],
 'installable': True,
 'application': False,
}
