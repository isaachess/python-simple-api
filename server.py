import web
import pydash as _
import random

##############
## Helpers ###
##############

def valueInEnum(value, allowedValues):
    return _.contains(allowedValues, value)

def valueInRange(value, allowedRange):
    return value >= allowedRange['min'] and value <= allowedRange['max']

#######################
### Response helpers ##
#######################

def genericFailure(message='Failure', statusCode=404):
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
    return genericFailure('The requested item is not available.')

def sendIfFound(item, successMessage='Success'):
    if item is None:
        return itemNotFound()
    else:
        return genericSuccess(item, successMessage)

###########
## CRUD ###
###########

operatingModes = ['cool', 'heat', 'off']
fanModes = ['off', 'auto']
coolSetpointRange = {'min': 30, 'max': 100}
heatSetpointRange = {'min': 30, 'max': 100}

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
        return genericSuccess(get(id))
    else:
        return genericFailure('Cannot update unknown resource.')

##################
## Model layer ###
##################

def getThermo(id):
    return sendIfFound(get(id))

def getProperty(id, prop):
    thermo = get(id)
    if thermo is None:
        return itemNotFound()
    value = thermo.get(prop, None)
    return sendIfFound(value)

def getName(id):
    return getProperty(id, 'name')

def setName(id, newName):
    return update(id, {'name': newName})

def getTemp(id):
    return getProperty(id, 'current_temp')

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
        newName = web.data()
        return setName(id, newName)

class temp:
    def GET(self, id):
        return getTemp(id)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
