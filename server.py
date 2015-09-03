import web
import lib
import constants as cst
import model
import response

#######################
## Routes and logic ###
#######################

def set_enum_value(id, prop, value, allowed_values):
    if lib.value_in_enum(value, allowed_values):
        return response.send_if_found(model.update(id, {prop: value}))
    else:
        return response.generic_failure('Cannot update: invalid value.', 400)

def set_range_value(id, prop, value, allowed_values):
    if lib.value_in_range(value, allowed_values):
        return response.send_if_found(model.update(id, {prop: value}))
    else:
        return response.generic_failure('Cannot update: invalid value.', 400)

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
        return response.send_if_found(model.get(id))

class name:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'name'))

    def PUT(self, id):
        new_name = web.data()
        return response.send_if_found(model.update(id, {'name': new_name}))

class temp:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'current_temp'))

class operating_mode:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'operating_mode'))

    def PUT(self, id):
        new_mode = web.data()
        return set_enum_value(id, 'operating_mode', new_mode, cst.operating_modes)

class cool_setpoint:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'cool_setpoint'))

    def PUT(self, id):
        num_setpoint = lib.convertToInt(web.data())
        return set_range_value(id, 'cool_setpoint', num_setpoint, cst.cool_setpoint_range)

class heat_setpoint:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'heat_setpoint'))

    def PUT(self, id):
        num_setpoint = lib.convertToInt(web.data())
        return set_range_value(id, 'heat_setpoint', num_setpoint, cst.heat_setpoint_range)

class fan_mode:
    def GET(self, id):
        return response.send_if_found(model.get_property(id, 'fan_mode'))

    def PUT(self, id):
        new_mode = web.data()
        return set_enum_value(id, 'fan_mode', new_mode, cst.fan_modes)

##################
## Run the app ###
##################

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
