from marshmallow import Schema, fields

class SavingsSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    group_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    last_updated = fields.DateTime(dump_only=True)