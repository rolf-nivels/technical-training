from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate properties"

    name = fields.Char(string="Name of the property", required=True, default="Unknown")
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char(string="Post code (ZIP)")
    date_availability = fields.Date(string="Availabilty date", default=lambda self: fields.Date.add(fields.Date.today(), months=+3), copy=False)
    expected_price = fields.Float(string="Price (expected)", required=True)
    selling_price = fields.Float(string="Price (selling)", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Size of bedrooms", default=2)
    living_area  = fields.Integer(string="Size of living area")
    facades = fields.Integer()
    garage = fields.Boolean(string="Garage available?")
    garden = fields.Boolean(string="Garden available?")
    garden_area = fields.Integer(string="Size of the garden")
    garden_orientation = fields.Selection([('north', 'North'), 
                                           ('south', 'South'),
                                           ('east', 'East'),
                                           ('west', 'West')])
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    state = fields.Selection([('new', 'New'), 
                              ('oreceived', 'Offer received'),
                              ('oaccepted', 'Offer accepted'),
                              ('sold', 'Sold'),
                              ('cancel', 'Canceled')], default='new')
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.partner", string="Salesman", required=True)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
