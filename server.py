import web
import lib
import constants as cst
import model

## names

def get_name(id):
    return model.get_property(id, 'name')

def set_name(id, new_name):
    return model.update(id, {'name': new_name})

## temp

def get_temp(id):
    return model.get_property(id, 'current_temp')

## operating mode

def get_operating_mode(id):
    return model.get_property(id, 'operating_mode')

def set_operating_mode(id, new_mode):
    return model.set_enum_value(id, 'operating_mode', new_mode, cst.operating_modes)

## cool setpoint

def get_cool_setpoint(id):
    return model.get_property(id, 'cool_setpoint')

def set_cool_setpoint(id, new_setpoint):
    num_setpoint = lib.convertToInt(new_setpoint)
    return model.set_range_value(id, 'cool_setpoint', num_setpoint, cst.cool_setpoint_range)

## heat setpoint

def get_heat_setpoint(id):
    return model.get_property(id, 'heat_setpoint')

def set_heat_setpoint(id, new_setpoint):
    num_setpoint = lib.convertToInt(new_setpoint)
    return model.set_range_value(id, 'heat_setpoint', num_setpoint, cst.heat_setpoint_range)

## fan mode

def get_fan_mode(id):
    return model.get_property(id, 'fan_mode')

def set_fan_mode(id, new_mode):
    return model.set_enum_value(id, 'fan_mode', new_mode, cst.fan_modes)

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
        return get_operating_mode(id)

    def PUT(self, id):
        new_mode = web.data()
        return set_operating_mode(id, new_mode)

class cool_setpoint:
    def GET(self, id):
        return get_cool_setpoint(id)

    def PUT(self, id):
        new_setpoint = web.data()
        return set_cool_setpoint(id, new_setpoint)

class heat_setpoint:
    def GET(self, id):
        return get_heat_setpoint(id)

    def PUT(self, id):
        new_setpoint = web.data()
        return set_heat_setpoint(id, new_setpoint)

class fan_mode:
    def GET(self, id):
        return get_fan_mode(id)

    def PUT(self, id):
        new_mode = web.data()
        return set_fan_mode(id, new_mode)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
