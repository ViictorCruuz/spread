from cornice import Service
from cornice.validators import marshmallow_body_validator
from pyramid.httpexceptions import HTTPCreated

from .....api.v1.resource.cors import cors_config

from .context import ClientCollectionFactory, ClientResourceFactory

from ..client.schemas import ClientSchema


"""Here we have an service that will create, update or get a client on database."""

client_collection = Service(
    name='clients',
    description='List all clients and created client on database',
    path='/api/v1/clients',
    factory=ClientCollectionFactory,
    **cors_config
)


client_resource = Service(
    name='client',
    description='Get a client',
    path='/api/v1/clients/{cpf}',
    factory=ClientResourceFactory,
    **cors_config
)


@client_collection.get(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def get_clients(request):
    clients = request.context.clients
    
    return ClientSchema().dump(clients, many=True)


@client_collection.post(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def create_client(request):
    new_client = Client(
        name=request.json_body['name'],
        cpf=request.json_body['cpf'],
        email=request.json_body['email']
    )
    
    request.tm.commit()
    
    return HTTPCreated(json=ClientSchema().dump(new_client))


@client_resource.get(
    validators=(marshmallow_body_validator,),
    content_type='application/json'
)
def get_client(request):
    client = request.context.client
    
    return ClientSchema().dump(client)
 