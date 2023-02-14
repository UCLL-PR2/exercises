def convert_to_fahrenheit(celsius_temp):
    return (9/5) * celsius_temp + 32

celsius_temps = [0, 10, 20, 30, 40]

def list_celsius_to_fahrenheit(celsius_temps):
    fahrenheit_temps = map(convert_to_fahrenheit, celsius_temps)
    return list(fahrenheit_temps)

