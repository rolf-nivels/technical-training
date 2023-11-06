from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate properties"

    name = fields.Char(string="Name of the property")
    description = fields.Text()
    postcode = fields.Char(string="Post code (ZIP)")
    date_availability = fields.Date(string="Availabilty date")
    expected_price = fields.Float(string="Price (expected)")
    selling_price = fields.Float(string="Price (selling)")
    bedrooms = fields.Integer(string="Size of bedrooms")
    living_area  = fields.Integer(string="Size of living area")
    facades = fields.Integer()
    garage = fields.Boolean(string="Garage available?")
    garden = fields.Boolean(string="Garden available?")
    garden_area = fields.Integer(string="Size of the garden")
    garden_orientation = fields.Selection([('north', 'North'), 
                                           ('south', 'South'),
                                           ('east', 'East'),
                                           ('west', 'West')])
