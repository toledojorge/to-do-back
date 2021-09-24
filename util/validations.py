from util.exceptions import RequiredValueException, ValueLenghtException

def validate_required(value, message):
    if value is None:
        raise RequiredValueException(message)

def validar_longitud(value, lenght, message):
    if len(value) > lenght:
        raise ValueLenghtException(message)