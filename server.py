import web
import pydash as _
import random

##############
## Helpers ###
##############

def value_in_enum(value, allowed_values):
    return _.contains(allowed_values, value)

def value_in_range(value, allowed_range):
    return value >= allowed_range['min'] and value <= allowed_range['max']

#######################
### Response helpers ##
#######################

def generic_failure(message='Failure', status_code=404):
    return {
        'message': message,
        'status_code': status_code
    }

def generic_success(payload, message='Success', status_code=200):
    return {
        'payload': payload,
        'message': message,
        'status_code': status_code
    }

def item_not_found():
    return generic_failure('The requested item is not available.')

def send_if_found(item, success_message='Success'):
    if item is None:
        return item_not_found()
    else:
        return generic_success(item, success_message)

###########
## CRUD ###
###########

operating_modes = ['cool', 'heat', 'off']
fan_modes = ['off', 'auto']
cool_setpoint_range = {'min': 30, 'max': 100}
heat_setpoint_range = {'min': 30, 'max': 100}

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
        return generic_success(get(id))
    else:
        return generic_failure('Cannot update unknown resource.')

##################
## Model layer ###
##################

def get_thermo(id):
    return send_if_found(get(id))

def get_property(id, prop):
    thermo = get(id)
    if thermo is None:
        return item_not_found()
    value = thermo.get(prop, None)
    return send_if_found(value)

def get_name(id):
    return get_property(id, 'name')

def set_name(id, new_name):
    return update(id, {'name': new_name})

def get_temp(id):
    return get_property(id, 'current_temp')

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
        return get_thermo(id)

class name:
    def GET(self, id):
        return get_name(id)

    def PUT(self, id):
        new_name = web.data()
        return set_name(id, new_name)

class temp:
    def GET(self, id):
        return get_temp(id)

class operating_mode:
    def GET(self, id):
        return getOperatingMode(id)

    def PUT(self, id):
        new_name = web.data()
        return set_name(id, new_name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
