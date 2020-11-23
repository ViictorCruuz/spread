from marshmallow import Schema, fields


class ClientSchema(Schema):
    
    name = fields.Str()
    cpf = fields.Str()
    email = fields.Email()
