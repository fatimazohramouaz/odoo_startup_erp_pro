from odoo import models, fields, api
class StartupSaleIntegration(models.Model):
    _name = 'startup.sale.integration'
    _description = 'Helpers to integrate sales and projects'

    @api.model
    def create_project_from_sale(self, sale_order):
        # Creates a project automatically when a sale order is confirmed (example helper)
        partner = sale_order.partner_id
        customer = self.env['startup.customer'].search([('partner_id','=',partner.id)], limit=1)
        if not customer:
            customer = self.env['startup.customer'].create({'name': partner.name, 'partner_id': partner.id})
        project = self.env['startup.project'].create({
            'name': sale_order.name,
            'customer_id': customer.id,
            'sale_order_id': sale_order.id,
            'budget': sum(line.price_subtotal for line in sale_order.order_line)
        })
        return project