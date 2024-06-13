# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = "material"
    _description = "Material"
    _sql_constraints = [
            ('code', 'unique(code)', 'Code already exists, please enter unique code'),
    ]

    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    material_type = fields.Selection(string="Type", selection=[
        ('fabric', 'Fabric'), 
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
     ], default="fabric", required=True)
    buy_price = fields.Float(string="Buy Price", required=True)
    supplier_id = fields.Many2one(comodel_name="supplier", string="Supplier", required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        if self.buy_price < 100:
            raise ValidationError("Buy price must be greater than equal to 100")
