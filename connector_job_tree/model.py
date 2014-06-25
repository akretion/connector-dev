# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Chafique DELLI
#    Copyright 2014 Akretion SA
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

from openerp.osv import orm, fields


class setdone_job(orm.TransientModel):
    _name = 'queue.setdone.job'
    _description = 'Wizard to set done a selection of jobs'

    def _get_job_ids(self, cr, uid, context=None):
        if context is None:
            context = {}
        res = False
        if (context.get('active_model') == 'queue.job' and
                context.get('active_ids')):
            res = context['active_ids']
        return res

    _columns = {
        'job_ids': fields.many2many('queue.job', string='Jobs'),
    }

    _defaults = {
        'job_ids': _get_job_ids,
    }

    def button_done(self, cr, uid, ids, context=None):
        if isinstance(ids, (tuple, list)):
            assert len(ids) == 1, "One ID expected"
            ids = ids[0]

        form = self.browse(cr, uid, ids, context=context)
        job_ids = [job.id for job in form.job_ids]
        self.pool.get('queue.job').button_done(cr, uid, job_ids, context=context)
        return {'type': 'ir.actions.act_window_close'}


class QueueJob(orm.Model):
    _inherit = 'queue.job'

    def extract_exc_info(self, cr, uid, ids, field_n, arg, context=None):
        res = {}
        for elm in self.browse(cr, uid, ids):
            exception = False
            if elm.exc_info:
                exception = elm.exc_info[:-1]
                last_position = exception.rfind('\n')
                pre_last_position = exception[:last_position].rfind('\n')
                if pre_last_position > 0:
                    exception = exception[pre_last_position:]
                else:
                    exception = exception[last_position:]
            res[elm.id] = exception
        return res

    _columns = {
        'exc_info_short': fields.function(
            extract_exc_info,
            string='Except short',
            type='text',
            store=False,
            help="Last lines of except message"),
    }

