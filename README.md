# python-simple-api
A simple python api using web.py

# Dependencies

- **web.py**: `sudo pip install web.py`

# API documentation

To run locally, simply run `python server.py` (by default listens on port `8080`)

This is a sample API for in-home thermostats. Everything is stored in memory, and starts with two thermostats available:

- Thermostat ID: `thermo1`
- Thermostat ID: `thermo2`

NOTE: When sending `PUT` requests, new values should be sent as raw values (i.e. not JSON) in the body.

## `/thermostat/:id`

- Supports: `GET`

## `/thermostat/:id/name`

- Supports: `GET`, `PUT`
- Data type: `string`

## `/thermostat/:id/temp`

- Support: `GET`
- Data type: `number`

NOTE: Since this is a sample app, it returns the same value every time.

## `/thermostat/:id/operating-mode`

- Supports: `GET`, `PUT`
- Data type: `string` (must be one of `cool`, `heat`, or `off`)

## `/thermostat/:id/cool-setpoint`

- Supports: `GET`, `PUT`
- Data type: `number` (must be in range of 30-100, stored in Fahrenheit)

## `/thermostat/:id/heat-setpoint`

- Supports: `GET`, `PUT`
- Data type: `number` (must be in range of 30-100, stored in Fahrenheit)

## `/thermostat/:id/fan-mode`

- Supports: `GET`, `PUT`
- Data type: `string` (must be one of `off` or `auto`)
