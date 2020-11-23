from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('cornice')

        config.include('pyramid_tm')

        config.include('.api')
        config.include('.routes')

    return config.make_wsgi_app()
