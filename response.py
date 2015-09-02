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

