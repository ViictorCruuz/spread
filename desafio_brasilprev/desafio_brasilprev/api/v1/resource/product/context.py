from .....models import DBSession

from .....models.client import Product
from pyramid.security import Allow, Everyone


class ProductCollectionFactory(object):
    def __init__(self, request):
        self.request = request
        self.products = DBSession.query(Product).all()

    # def __acl__(self):
    #     return [(Allow, Everyone, ['view', 'create', 'edit'])]


class ProductResourceFactory(object):
    def __init__(self, request):
        self.product = DBSession.query(Product).filter_by(code=request.matchdict['p_code']).one()

    # def __acl__(self):
    #     return [(Allow, Everyone, ['view', 'create', 'edit'])]
