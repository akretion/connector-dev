# -*- coding: utf-8 -*-
########################################################################
#
#  licence AGPL version 3 or later : see __openerp__.py file
#  Copyright (C) 2014 Akretion (http://www.akretion.com).
#  @author David BEAL <david.beal@akretion.com>
#
########################################################################

from openerp.osv import orm
import os


class AbstractConnectorLink(orm.AbstractModel):
    _inherit = 'abstract.connector.link'

    def _get_map_external_model(self, cr, uid, model, task, context=None):
        model_map = {
            'magento.sale.order': 'sales_order/view/order_id',
        }
        res = ''
        if model in model_map:
            if model == 'magento.sale.order':
                start_task_string = task.find(model + "', ") + 21
                backend_id, order_increm = task[start_task_string:-1].split(',')
                backend = self.pool['magento.backend'].browse(
                    cr, uid, int(backend_id), context=context)
                if backend.external_backend_url:
                    order_increm = order_increm.replace(' ', '').replace("'", '')
                    res = os.path.join(backend.external_backend_url,
                                       model_map[model], order_increm)
        return res
