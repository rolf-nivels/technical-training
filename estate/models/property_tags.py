from odoo import models, fields

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Estate property tag"

    name = fields.Char(required=True)
