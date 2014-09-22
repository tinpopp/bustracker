MONGO_HOST = 'localhost'
# MONGO_HOST = '192.168.137.1'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'bustrackerserver'
SERVER_NAME = None

IF_MATCH = False
HATEOAS = False
PAGINATION = False
SORTING = False

schema = {
	'busNo': {
        'type': 'string',
        'maxlength': 2,
		'unique': True,
    },
    'latitude': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'longitude': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'routeNo': {
        'type': 'string',
        'maxlength': 2,
    },
    'status': {
        'type': 'string',
        'maxlength': 30,
    },
}

buses = {
    'item_title': 'bus',
    'resource_methods': ['GET', 'POST'],
	'public_methods': ['GET', 'POST'],
	'item_methods': ['GET','PATCH','PUT', 'DELETE'],
	'public_item_methods': ['GET','PATCH','PUT', 'DELETE'],
    'schema': schema,
}

DOMAIN = {
    'buses': buses,
}