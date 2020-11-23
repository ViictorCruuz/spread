from marshmallow import Schema, fields


class BrazilianCurrency(fields.Decimal):

    def _serialize(self, value, attr, obj, **kwargs):
        return 'R$ {}'.format(str(value).replace('.', ','))


class ProductSchema(Schema):
    
    name = fields.Str()
    code = fields.Int()
    price = BrazilianCurrency()
