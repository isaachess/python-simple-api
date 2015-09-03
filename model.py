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
        'fan_mode': 'off'
    }
}

def get(id):
    return thermostats.get(id, None)

def update(id, updates):
    if id in thermostats:
        for key in updates:
            thermostats[id][key] = updates[key]
        return get(id)
    else:
        return None

def get_property(id, prop):
    thermo = get(id)
    if thermo is None:
        return None
    return thermo.get(prop, None)
