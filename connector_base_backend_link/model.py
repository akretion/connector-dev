# -*- coding: utf-8 -*-
########################################################################
#
#  licence AGPL version 3 or later : see __openerp__.py file
#  Copyright (C) 2014 Akretion (http://www.akretion.com).
#  @author David BEAL <david.beal@akretion.com>
#
########################################################################

from openerp.osv import orm, fields


class ConnectorBackend(orm.Model):
    _inherit = 'connector.backend'

    _columns = {
        'external_backend_url': fields.char(
            'External Backend Url',
            help="Base url used to define contextual url link "
                 "towards external backend of the application "
                 "connected to openerp",)
    }


class AbstractConnectorLink(orm.AbstractModel):
    _name = 'abstract.connector.link'

    def _get_url_according_to_model(self, cr, uid, ids, field_n, arg, context=None):
        return {}

    def __get_url_according_to_model(self, cr, uid, ids, field_n, arg, context=None):
        return self._get_url_according_to_model(cr, uid, ids, field_n, arg, context=context)

    _columns = {
        'backend_link': fields.function(
            __get_url_according_to_model,
            string='magento',
            type='char',
            store=False,
            help="External link"),
    }

    def _get_map_external_model(self, cr, uid, model, task, context=None):
        return {}


class QueueJob(orm.Model):
    _inherit = ['queue.job', 'abstract.connector.link']
    _name = 'queue.job'

    def _get_url_according_to_model(self, cr, uid, ids, field_n, arg, context=None):
        res = {}
        for elm in self.browse(cr, uid, ids):
            if elm.model_name:
                result = self.pool['abstract.connector.link']._get_map_external_model(
                    cr, uid, elm.model_name, elm.func_string, context=context)
                res[elm.id] = result
            if elm.id not in res:
                res[elm.id] = 'no url specified'
        return res


class SaleOrder(orm.Model):
    _inherit = ['sale.order', 'abstract.connector.link']
    _name = 'sale.order'

    def _get_url_according_to_model(self, cr, uid, ids, field_n, arg, context=None):
        res = {}
        for elm in self.browse(cr, uid, ids):
            if elm.magento_bind_ids:
                backend = elm.magento_bind_ids[0].backend_id
                if backend.external_backend_url:
                    val = backend.external_backend_url + str(elm.magento_bind_ids[0].magento_order_id)
                res[elm.id] = val
            if elm.id not in res:
                res[elm.id] = 'no url specified'
        return res
