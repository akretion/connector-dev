# -*- coding: utf-8 -*-
# Copyright 2013 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.queue_job.job import Job
from openerp import api, fields, models


class QueueJob(models.Model):
    _inherit = 'queue.job'

    def run_now(self):
        for job in self:
            Job.load(self.env, job.uuid).perform()
            job.state = 'done'
        return True
