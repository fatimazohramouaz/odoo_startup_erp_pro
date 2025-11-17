from odoo import models, fields, api
class CreateInvoiceWizard(models.TransientModel):
    _name = 'startup.create.invoice.wizard'
    project_id = fields.Many2one('startup.project', required=True)
    create_and_open = fields.Boolean(default=True)

    def action_create_invoice(self):
        self.ensure_one()
        invoice = self.project_id.create_invoice_from_project()
        if self.create_and_open:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': invoice.id,
            }
        return {'type':'ir.actions.act_window_close'}