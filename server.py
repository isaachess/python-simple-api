import web
import pydash as _

###########
## CRUD ###
###########

thermostats = {
    'thermo1': {
        'id': 'thermo1',
        'name': 'x-wing',
        'current_temp': 78,
        'operating_mode': 'cool',
        'cool_setpoint': 75,
        'head_setpoint': 78,
        'fan_mode': 'auto'
    },
    'thermo2': {
        'id': 'thermo1',
        'name': 'y-wing',
        'current_temp': 75,
        'operating_mode': 'heat',
        'cool_setpoint': 70,
        'head_setpoint': 77,
        'fan_mode': 'auto'
    }
}

def get(id):
    return thermostats.get(id, None)

def update(id, updates):
    if id in thermostats:
        thermostats[id] = _.merge(thermostats[id], updates)
        return None
    else:
        return None

#######################
### Response helpers ##
#######################

def genericFailure(message='Failure', statusCode=400):
    return {
        'message': message,
        'statusCode': statusCode
    }

def genericSuccess(payload, message='Success'):
    return {
        'payload': payload,
        'message': message
    }

def itemNotFound():
    return genericFailure('The requested item is not available.', 404)

def sendIfFound(item, successMessage='Success'):
    if item is None:
        return itemNotFound()
    else:
        return genericSuccess(item, successMessage)

##################
## Model layer ###
##################

def getThermo(id):
    return sendIfFound(get(id))

def getName(id):
    thermo = get(id)
    if thermo is None:
        return itemNotFound()
    name = thermo.get('name', None)
    return sendIfFound(name)

##############
## Routing ###
##############

urls = (
    '/thermostat/(\w+)', 'thermostat',
    '/thermostat/(\w+)/name', 'name',
    '/thermostat/(\w+)/temp', 'temp',
    '/thermostat/(\w+)/operating-mode', 'operating_mode',
    '/thermostat/(\w+)/cool-setpoint', 'cool_setpoint',
    '/thermostat/(\w+)/heat-setpoint', 'heat_setpoint',
    '/thermostat/(\w+)/fan-mode', 'fan_mode',
)

class thermostat:
    def GET(self, id):
        return getThermo(id)

class name:
    def GET(self, id):
        return getName(id)

    def PUT(self, id):
        name = web.data()
        return 'you put'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
