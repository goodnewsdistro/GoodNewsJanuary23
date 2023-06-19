# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    last_order_date = fields.Datetime(compute='_compute_last_order_date', string='Last Order Date')

    @api.depends('sale_order_ids')
    def _compute_last_order_date(self):
        for record in self:
            last_order = self.env['sale.order'].search([('partner_id', '=', record.id)], order='date_order desc', limit=1)
            if last_order:
                record.last_order_date = last_order.date_order
            else:
                record.last_order_date = False
