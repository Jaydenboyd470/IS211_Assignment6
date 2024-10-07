class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        'Celsius': {'Kelvin': lambda x: x + 273.15, 'Fahrenheit': lambda x: x * 9/5 + 32, 'Celsius': lambda x: x},
        'Fahrenheit': {'Celsius': lambda x: (x - 32) * 5/9, 'Kelvin': lambda x: (x - 32) * 5/9 + 273.15, 'Fahrenheit': lambda x: x},
        'Kelvin': {'Celsius': lambda x: x - 273.15, 'Fahrenheit': lambda x: (x - 273.15) * 9/5 + 32, 'Kelvin': lambda x: x},
        'Miles': {'Yards': lambda x: x * 1760, 'Meters': lambda x: x * 1609.34, 'Miles': lambda x: x},
        'Yards': {'Miles': lambda x: x / 1760, 'Meters': lambda x: x * 0.9144, 'Yards': lambda x: x},
        'Meters': {'Miles': lambda x: x / 1609.34, 'Yards': lambda x: x / 0.9144, 'Meters': lambda x: x},
    }

    if fromUnit in conversions and toUnit in conversions[fromUnit]:
        return conversions[fromUnit][toUnit](value)
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible")
