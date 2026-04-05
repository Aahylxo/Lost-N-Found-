from odoo import models, fields, api

class FoundItem(models.Model):
    _name = "found.item"
    _description = "Found Item list"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Item Description", required=True, tracking=True)
    ref_id = fields.Char(string="Tracking ID", readonly=True, copy=False, default="New")
    
    tag_ids = fields.Many2many('item.tag', string="Tags")

    # Some Common areas where they could loose things @>XO<@
    location = fields.Selection([
        ('gym', 'GYM'),
        ('auditorium', 'Auditorium'),
        ('1st_floor', '1st Floor'),
        ('2nd_floor', '2nd Floor'),
        ('3rd_florr','3rd Floor'),
        ('hallway', 'Hallway'),
        ('main_lobby', 'Main Lobby'),
        ('cash_register', 'Cash Register'),
        ('cafeteria', 'Cafeteria'),
        ('library', 'Library'),
        ('campus_grounds', 'Outdoor Campus Grounds') 
    ], string="Location", required=True)
    

    date = fields.Date(string="Date", required=True, default=fields.Date.context_today)
    photo = fields.Image(string="Item Photo(s)", max_width=1024, max_height=1024)

    status = fields.Selection([
        ('logged', 'Logged'),
        ('matched', 'Matched'),
        ('resolved', 'Resolved'),
        ('donated', 'Donated')
    ], string="Status", default='logged', tracking=True)

    def action_resolve(self):
        for record in self:
            record.status = 'resolved'
        return True

    def action_donate(self):
        for record in self:
            record.status = 'donated'
        return True
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ref_id', 'New') == 'New':
                total_items = self.search_count([])
                next_number = total_items + 1
                vals['ref_id'] = f"FND/{next_number:03d}"
        return super().create(vals_list)
