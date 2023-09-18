from marshmallow import Schema, fields

class EmailSchema(Schema):

    subject = fields.Str(required=True)
    to = fields.Email(required=True)
    body = fields.Str(required=True)