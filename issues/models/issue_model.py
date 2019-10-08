from odoo import api,fields,models

class Issue(models.Model):
    _name = "issue_new.model"
    _description = "Issue Management"
    _inherit = ["mail.thread"]

    cust_name = fields.Many2one("res.partner",string="Customer Name")
    title = fields.Char("Title")
    desc = fields.Text(string="Description",size=100,default="Description")
    product = fields.Many2one("product.product",string="Product")
    date = fields.Date(string="Date")
    color = fields.Integer('Color Index')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority', default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban State', default='normal')

    """
    def _default_sales_person(self):
        return self.env["res.partner"].search([("name","=",self.cust_name.name)], limit=1).id
    """

    proof = fields.Binary("Proof/Evidence",store=True)
    salesperson = fields.Many2one("res.partner",string="Salesperson")
    assign_to = fields.Many2many("res.partner",string="Assign To")
    stage_id = fields.Many2one("issue.stage","Stage")
    issue_state = fields.Selection(related='stage_id.state', string='Stage State')



class Tag(models.Model):
    _name = "issue.tag"
    _description = "Severity tag"

    tag_name = fields.Char(string="Name")
    expected_closing = fields.Date(string="Close issue by")

class Stage(models.Model):
    _name = "issue.stage"
    _description = "stages an issue goes through"

    name = fields.Char("Name")
    desc = fields.Text("Description")
    state = fields.Selection([('new', 'New'), ('pending', 'Pending'), ('solved', 'Solved')], 'State')
    issues = fields.One2many("issue_new.model", "stage_id","Issues in this stage")
