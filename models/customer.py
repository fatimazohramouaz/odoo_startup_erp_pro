from odoo import models, fields, api
class StartupCustomer(models.Model):
    _name = 'startup.customer'
    _description = 'Customer for the startup'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    email = fields.Char(tracking=True)
    phone = fields.Char()
    company_name = fields.Char()
    partner_id = fields.Many2one('res.partner', string='Partner')
    projects_count = fields.Integer(compute='_compute_projects_count')

   
    def _compute_projects_count(self):
        for rec in self:
            rec.projects_count = self.env['startup.project'].search_count([('customer_id','=',rec.id)])