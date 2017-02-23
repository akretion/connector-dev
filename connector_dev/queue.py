# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Sebastien BEAU
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
#############################################################################

import traceback
from StringIO import StringIO

from openerp.osv import orm
from openerp.addons.connector.queue.job import OpenERPJobStorage
from openerp.addons.connector.session import ConnectorSession
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

from datetime import datetime

class QueueJob(orm.Model):
    _inherit = 'queue.job'

    def run_now(self, cr, uid, ids, context=None):
        for oe_job in self.browse(cr, SUPERUSER_ID, ids, context=context):
            session = ConnectorSession(cr, oe_job.user_id.id, context=context)
            storage = OpenERPJobStorage(session)
            job = storage.load(oe_job.uuid)
            try:
                job.perform(session)
            except:
                buff = StringIO()
                traceback.print_exc(file=buff)
                #job.set_failed(exc_info=buff.getvalue())
                #job.state = 'failed'
                #storage.store(job)
                oe_job.write({
                    'state': 'failed',
                    'exc_info': buff.getvalue()    
                })
                raise
            oe_job.write({
                'state': 'done',
                'date_done': datetime.now().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
            })
        return True

    def run_queue_job_cron(self, cr, uid, ids, context=None):
        cron_id = self.pool['ir.model.data'].get_object_reference(
            cr, uid, 'connector', 'ir_cron_enqueue_jobs')[1]
        self.pool['ir.cron'].run_manually(cr, uid, [cron_id], context=context)
        return True
