import response
import pydash as _
import lib

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
        'heat_setpoint': 78,
        'fan_mode': 'auto'
    },
    'thermo2': {
        'id': 'thermo1',
        'name': 'y-wing',
        'current_temp': 75,
        'operating_mode': 'heat',
        'cool_setpoint': 70,
        'heat_setpoint': 77,
        'fan_mode': 'auto'
    }
}

def get(id):
    return thermostats.get(id, None)

def update(id, updates):
    if id in thermostats:
        thermostats[id] = _.merge(thermostats[id], updates)
        return response.generic_success(get(id))
    else:
        return response.generic_failure('Cannot update: item not found.')

##################
## Model layer ###
##################

## Low-level model helpers

def get_thermo(id):
    return response.send_if_found(get(id))

def get_property(id, prop):
    thermo = get(id)
    if thermo is None:
        return response.item_not_found()
    value = thermo.get(prop, None)
    return response.send_if_found(value)

def set_enum_value(id, prop, value, allowed_values):
    if lib.value_in_enum(value, allowed_values):
        return update(id, {prop: value})
    else:
        return response.generic_failure('Cannot update: invalid value.', 400)

def set_range_value(id, prop, value, allowed_values):
    if lib.value_in_range(value, allowed_values):
        return update(id, {prop: value})
    else:
        return response.generic_failure('Cannot update: invalid value.', 400)

