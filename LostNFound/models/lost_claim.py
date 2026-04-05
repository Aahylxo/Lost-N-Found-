from odoo import models, fields, api

class LostClaim(models.Model):
    _name = "lost.claim"
    _description = "Lost Item Claim"
    _inherit = ['mail.thread']
    
    # Student Details
    person_name = fields.Char(string="Student Name", required=True)
    contact_email = fields.Char(string="Contact Email", required=True)

    # Item Details
    name = fields.Char(string="What did you lose?", required=True)
    
    tag_ids = fields.Many2many('item.tag', string="Tags")
    
    date_lost = fields.Date(string="Date Lost", default=fields.Date.context_today, required=True)
    location = fields.Selection([
        ('gym', 'GYM'),
        ('auditorium', 'Auditorium'),
        ('1st_floor', '1st Floor'),
        ('2nd_floor', '2nd Floor'),
        ('3rd_floor','3rd Floor'),
        ('hallway', 'Hallway'),
        ('main_lobby', 'Main Lobby'),
        ('cash_register', 'Cash Register'),
        ('cafeteria', 'Cafeteria'),
        ('library', 'Library'),
        ('campus_grounds', 'Outdoor Campus Grounds')  
    ], string="Where do you think you left it?", required=True)

    # The Link! (This connects the Claim to the Found Item)
    matched_item_id = fields.Many2one('found.item', string="Matched Found Item", readonly=True)

    status = fields.Selection([
        ('submitted', 'Submitted'),
        ('investigating', 'Investigating'),
        ('matched', 'Match Found!'),
        ('closed', 'Closed')
    ], string="Status", default='submitted')

    def action_find_match(self):
            for claim in self:
                if not claim.tag_ids:
                    continue

                match = self.env['found.item'].search([
                    ('status', '=', 'logged'),               
                    ('tag_ids', 'in', claim.tag_ids.ids),
                    ('name','ilike',claim.name)    
                ], limit=1)                                  

                if match:
                    claim.matched_item_id = match.id
                    claim.status = 'matched'
                    match.status = 'matched' 

                    # We check if the student actually provided an email
                    if claim.contact_email:
                        # We write the email subject and body
                        subject = f"Match Found for your {claim.name}!"
                        body = f"""
                            Hello {claim.person_name},<br><br>
                            Great news! We believe we have found your <b>{claim.name}</b>.<br>
                            It was found near: {match.location}.<br><br>
                            Please come to the campus security desk with your student ID to claim it.
                        """
                        self.env['mail.mail'].create({
                                'subject': subject,
                                'body_html': body,
                                'email_to': claim.contact_email,
                        }).send()
            return True
