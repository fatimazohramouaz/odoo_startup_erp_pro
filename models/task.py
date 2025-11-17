from odoo import models, fields, api
class StartupTask(models.Model):
    _name = 'startup.task'
    _description = 'Task inside a project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    project_id = fields.Many2one('startup.project', string='Project')
    assigned_to = fields.Many2one('res.users', string='Assigned to')
    planned_hours = fields.Float()
    spent_hours = fields.Float()
    stage = fields.Selection([('todo','To Do'),('doing','Doing'),('done','Done')], default='todo', tracking=True)
    note = fields.Text()

    progress = fields.Float(string='Progress (%)', compute='_compute_progress', store=True)

    @api.depends('spent_hours','planned_hours')
    def _compute_progress(self):
        for rec in self:
            if rec.planned_hours:
                rec.progress = min(100, (rec.spent_hours / rec.planned_hours) * 100)
            else:
                rec.progress = 0