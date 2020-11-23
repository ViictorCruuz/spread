"""Api v1 config module."""


def includeme(config):

    config.include('.client')
    config.include('.product')

    config.scan()
