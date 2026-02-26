def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def convert_temperature(temperature, unit):
    if unit == 'C':
        converted_temperature = celsius_to_fahrenheit(temperature)
        return converted_temperature
    elif unit == 'F':
        converted_temperature = fahrenheit_to_celsius(temperature)
        return converted_temperature
    else:
        pass