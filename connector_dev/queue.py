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

from openerp.osv import orm, fields
from openerp.addons.connector.queue.job import OpenERPJobStorage
from openerp.addons.connector.session import ConnectorSession


class QueueJob(orm.Model):
    _inherit = 'queue.job'

    def get_traceback_last_line(self, cr, uid, ids, field_n, arg, context=None):
        res = {}
        for elm in self.browse(cr, uid, ids):
            trace = elm.exc_info
            if trace:
                position = trace[:-1].rfind('\n') + 1
                res[elm.id] = {field_n: trace[position:-1]}
        return res

    _columns = {
        'exc_info_last_line': fields.function(
            get_traceback_last_line,
            string='Traceback',
            type='unicode',
            store=False),
    }

    def run_now(self, cr, uid, ids, context=None):
        session = ConnectorSession(cr, uid, context=context)
        storage = OpenERPJobStorage(session)
        for oe_job in self.browse(cr, uid, ids, context=context):
            job = storage.load(oe_job.uuid)
            job.perform(session)
            oe_job.write({'state': 'done'})
        return True

    def run_queue_job_cron(self, cr, uid, ids, context=None):
        cron_id = self.pool['ir.model.data'].get_object_reference(
            cr, uid, 'connector', 'ir_cron_enqueue_jobs')[1]
        self.pool['ir.cron'].run_manually(cr, uid, [cron_id], context=context)
        return True
