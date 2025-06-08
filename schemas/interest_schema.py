from marshmallow import Schema, fields

class InterestSchema(Schema):
    id = fields.Int(dump_only=True)
    savings_id = fields.Int(required=True)
    interest_amount = fields.Float(required=True)
    rate = fields.Float(required=True)
    calculated_on = fields.DateTime(dump_only=True)