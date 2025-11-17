from odoo import models, fields, api
class StartupProject(models.Model):
    _name = 'startup.project'
    _description = 'Project for client'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    customer_id = fields.Many2one('startup.customer', string='Customer', tracking=True)
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    description = fields.Text()
    manager_id = fields.Many2one('res.users', string='Project Manager')
    start_date = fields.Date()
    end_date = fields.Date()
    state = fields.Selection([('draft','Draft'),('in_progress','In Progress'),('done','Done'),('cancel','Cancelled')], default='draft', tracking=True)
    task_ids = fields.One2many('startup.task','project_id', string='Tasks')
    budget = fields.Float()

    invoice_count = fields.Integer(compute='_compute_invoice_count')

    def action_start(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def _compute_invoice_count(self):
        for rec in self:
            rec.invoice_count = self.env['account.move'].search_count([('invoice_origin','=',rec.name)])

    def create_invoice_from_project(self):
        # Creates a simple invoice by linking to project name as origin.
        self.ensure_one()
        sale = self.sale_order_id
        invoice_vals = {
            'move_type': 'out_invoice',
            'invoice_date': fields.Date.today(),
            'invoice_origin': self.name,
            'partner_id': self.customer_id.partner_id.id if self.customer_id.partner_id else False,
            'invoice_line_ids': [(0,0, {'name': 'Project: %s' % self.name, 'quantity':1, 'price_unit': self.budget or 0.0})]
        }
        invoice = self.env['account.move'].create(invoice_vals)
        return invoice