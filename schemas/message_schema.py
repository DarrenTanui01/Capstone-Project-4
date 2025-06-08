from marshmallow import Schema, fields

class MessageSchema(Schema):
    id = fields.Int(dump_only=True)
    group_id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    content = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True)