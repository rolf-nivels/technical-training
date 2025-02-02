from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"

    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], string="Status", copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Estate property", required=True)
