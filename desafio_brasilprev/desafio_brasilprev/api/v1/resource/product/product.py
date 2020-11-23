from cornice import Service
from cornice.validators import marshmallow_body_validator
from pyramid.httpexceptions import HTTPCreated

from .....models.client import Product

from .....api.v1.resource.cors import cors_config

from ..product.schemas import ProductSchema

from ...resource.product.context import ProductCollectionFactory, ProductResourceFactory

product_collection = Service(
    name='product',
    description='Create and get product on database',
    path='/api/v1/products',
    factory=ProductCollectionFactory,
    **cors_config
)

product = Service(
    name='single product',
    description='Create and get product on database',
    path='/api/v1/products/{p_code}',
    factory=ProductResourceFactory,
    **cors_config
)


@product_collection.get(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def list_products(request):
    products = request.context.products

    return ProductSchema().dump(products, many=True)


@product_collection.post(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def create_product(request):

    new_product = Product(
        name=request.json_body['name'],
        code=request.json_body['code'],
        price=request.json_body['price']
    )

    request.tm.commit()

    return HTTPCreated(json=ProductSchema().dump(new_product))


@product.get(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def get_product(request):
    product = request.context.product

    return ProductSchema().dump(product)
