from odoo import models, fields, api

class FoundItem(models.Model):
    _name = "found.item"
    _description = "Found Item list"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string = "Item Description", required=True, tracking = True)
    ref_id  = fields.Char(string="Tracking ID",readonly =True, copy=False, default="New")

    category = fields.Selection([
        ('electronics','Electronics(Phone, Laptop)'),
        ('clothing','Clothing & Accessories'),
        ('documents','IDs, Wallets & Keys'),
        ('other','Other')
    ],string = "Category",required = True, tracking = True)

    location = fields.Char(string = "Location Found", required =True)
    date = fields.Date(string="Date", required=True, defaul=lambda self: self.env.user)

    photo = fields.Image(string="Item Photo(s)",max_width = 1024, max_height=1024)

    status = fields.Selection([
        ('logged','Logged'),
        ('matched','Matched'),
        ('resovled','Resolved'),
        ('donated','Donated')
    ],string ="Status",default='logged',tracking=True)

    def action_resolve(self):
        for record in self:
            record.status = 'resolved'
        return True

    def action_donate(self):
        for record in self:
            record.status = 'donated'
        return True