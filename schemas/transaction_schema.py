from marshmallow import Schema, fields

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    group_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    type = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True)
    description = fields.Str()