from odoo import models, fields, api
class StartupHRExtension(models.Model):
    _inherit = 'hr.employee'

    is_startup_dev = fields.Boolean(string='Developer in Startup')
    github_username = fields.Char(string='GitHub Username')