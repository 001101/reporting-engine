# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class IrActionsReportXml(models.Model):
    _inherit = 'ir.actions.report.xml'

    @api.model
    def _check_selection_field_value(self, field, value):
        if field == 'report_type' and value == 'xlsx':
            return
        return super(IrActionsReportXml, self).\
            _check_selection_field_value(field, value)
