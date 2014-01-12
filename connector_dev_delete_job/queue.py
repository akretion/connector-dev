# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: David BEAL
#    Copyright 2014 Akretion SARL
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

from openerp.osv import orm


class QueueJob(orm.Model):
    _inherit = 'queue.job'

    def delete_failed_jobs(self, cr, uid, ids, context=None):
        job_ids = self.search(
            cr, uid, [('state', '=', 'failed')], context=context)
        self.unlink(cr, uid, job_ids, context=context)

    def delete_done_jobs(self, cr, uid, ids, context=None):
        job_ids = self.search(
            cr, uid, [('state', '=', 'done')], context=context)
        self.unlink(cr, uid, job_ids, context=context)
