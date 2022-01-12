# Copyright 2013 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{'name': 'Connector dev',
 'version': '14.0.1.0.0',
 'author': 'Openerp Connector Core Editors',
 'website': 'https://launchpad.net/openerp-connector',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
.Helper to connector to retry instantly to perform a job.
It add a button in backend to retry failed job.
""",
 'depends': [
     'queue_job',
 ],
 'data': [
     'job_view.xml',
 ],
 'installable': True,
 'application': False,
}
