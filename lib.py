def value_in_enum(value, allowed_values):
    return value in allowed_values

def value_in_range(value, allowed_range):
    return value >= allowed_range['min'] and value <= allowed_range['max']

def convertToInt(value):
    try:
        return int(float(value))
    except ValueError:
        return None
