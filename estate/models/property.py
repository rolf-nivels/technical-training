from odoo import api, models, fields

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
    salesman_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Property offers")
    total_area = fields.Integer(string="Total Area (sqm)", compute="_compute_area")
    best_price = fields.Float(string="Best price", compute="_compute_best_price", store=True)


    @api.depends("living_area","garden_area")
    def _compute_area(self):
        for rec in self:
            rec.total_area += rec.living_area + rec.garden_area


    @api.depends("offer_ids")
    def _compute_best_price(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_price = max(rec.offer_ids.mapped('price'))

