from django.core.exceptions import ValidationError
import re


def validate_first_name(value):
    first_name = str(value)
    if not re.match("^[A-Za-z]*$", first_name):
        raise ValidationError("Enter only alphabats")
    return value

def validate_last_name(value):
    last_name = str(value)
    if not re.match("^[A-Za-z]*$", last_name):
        raise ValidationError("Enter only alphabats")
    return value

def validate_mobile_no(value):
    mobile_no = str(value)
    if not re.match("^[0-9]*$", mobile_no):
        raise ValidationError("Enter only numbers")
    return value


def validate_phone_no(value):
    phone_no = str(value)
    if not re.match("^[0-9]*$", phone_no):
        raise ValidationError("Enter only numbers")
    return value

def validate_city(value):
    city = str(value)
    if not re.match("^[A-Za-z]*$", city):
        raise ValidationError("Enter only alphabats")
    return value

def validate_state(value):
    state = str(value)
    if not re.match("^[A-Za-z]*$", state):
        raise ValidationError("Enter only alphabats")
    return value

def validate_landmark(value):
    landmark = str(value)
    if not re.match("^[A-Za-z]*$", landmark):
        raise ValidationError("Enter only alphabats")
    return value
def validate_education(value):
    education = str(value)
    if not re.match("^[A-Za-z0-9.]*$", education):
        raise ValidationError("Enter only alphabats and numbers")
    return value
def validate_specelization(value):
    specialization = str(value)
    if not re.match("^[A-Za-z\s]*$", specialization):
        raise ValidationError("Enter only alphabats")
    return value
def validate_media_name(value):
    media_name = str(value)
    if not re.match("^[A-Za-z]*$", media_name):
        raise ValidationError("Enter only alphabats")
    return value
def validate_loc_name(value):
    loc_name = str(value)
    if not re.match("^[A-Za-z]*$", loc_name):
        raise ValidationError("Enter only alphabats")
    return value
def validate_name(value):
    name = str(value)
    if not re.match("^[A-Za-z]*$", name):
        raise ValidationError("Enter only alphabats")
    return value