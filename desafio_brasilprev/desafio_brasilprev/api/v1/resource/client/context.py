from .....models import DBSession
from .....models.client import Client


class ClientCollectionFactory(object):
    def __init__(self, request):
        self.clients = DBSession.query(Client).all()


class ClientResourceFactory(object):
    def __init__(self, request):
        cpf = request.matchdict['cpf']
        self.client = DBSession.query(Client).filter_by(cpf=cpf).one()
