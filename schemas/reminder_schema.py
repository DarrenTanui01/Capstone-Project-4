from marshmallow import Schema, fields

class ReminderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    group_id = fields.Int(required=True)
    message = fields.Str(required=True)
    due_date = fields.DateTime(required=True)
    sent = fields.Bool()