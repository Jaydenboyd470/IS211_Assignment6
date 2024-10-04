# Import the functions from conversions.py
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)

# Test for Celsius to Kelvin and Fahrenheit (from Part I and II)
def test_convertCelsiusToKelvin():
    print("Testing convertCelsiusToKelvin...")
    assert convertCelsiusToKelvin(300.00) == 573.15, "Test case 1 failed"
    assert convertCelsiusToKelvin(0.00) == 273.15, "Test case 2 failed"
    assert convertCelsiusToKelvin(100.00) == 373.15, "Test case 3 failed"
    assert convertCelsiusToKelvin(-273.15) == 0.00, "Test case 4 failed"
    assert convertCelsiusToKelvin(25.00) == 298.15, "Test case 5 failed"
    print("All convertCelsiusToKelvin test cases passed")

def test_convertCelsiusToFahrenheit():
    print("Testing convertCelsiusToFahrenheit...")
    assert convertCelsiusToFahrenheit(300.00) == 572.00, "Test case 1 failed"
    assert convertCelsiusToFahrenheit(0.00) == 32.00, "Test case 2 failed"
    assert convertCelsiusToFahrenheit(100.00) == 212.00, "Test case 3 failed"
    assert convertCelsiusToFahrenheit(-40.00) == -40.00, "Test case 4 failed"
    assert convertCelsiusToFahrenheit(25.00) == 77.00, "Test case 5 failed"
    print("All convertCelsiusToFahrenheit test cases passed")

# New Tests for Part III

# Test for Fahrenheit to Celsius
def test_convertFahrenheitToCelsius():
    print("Testing convertFahrenheitToCelsius...")
    assert convertFahrenheitToCelsius(32.00) == 0.00, "Test case 1 failed"
    assert convertFahrenheitToCelsius(212.00) == 100.00, "Test case 2 failed"
    assert convertFahrenheitToCelsius(-40.00) == -40.00, "Test case 3 failed"
    assert convertFahrenheitToCelsius(98.60) == 37.00, "Test case 4 failed"
    assert convertFahrenheitToCelsius(572.00) == 300.00, "Test case 5 failed"
    print("All convertFahrenheitToCelsius test cases passed")

# Test for Fahrenheit to Kelvin
def test_convertFahrenheitToKelvin():
    print("Testing convertFahrenheitToKelvin...")
    assert convertFahrenheitToKelvin(32.00) == 273.15, "Test case 1 failed"
    assert convertFahrenheitToKelvin(212.00) == 373.15, "Test case 2 failed"
    assert convertFahrenheitToKelvin(-40.00) == 233.15, "Test case 3 failed"
    assert convertFahrenheitToKelvin(572.00) == 573.15, "Test case 4 failed"
    assert convertFahrenheitToKelvin(98.60) == 310.15, "Test case 5 failed"
    print("All convertFahrenheitToKelvin test cases passed")

# Test for Kelvin to Celsius
def test_convertKelvinToCelsius():
    print("Testing convertKelvinToCelsius...")
    assert convertKelvinToCelsius(273.15) == 0.00, "Test case 1 failed"
    assert convertKelvinToCelsius(373.15) == 100.00, "Test case 2 failed"
    assert convertKelvinToCelsius(0.00) == -273.15, "Test case 3 failed"
    assert convertKelvinToCelsius(298.15) == 25.00, "Test case 4 failed"
    assert convertKelvinToCelsius(573.15) == 300.00, "Test case 5 failed"
    print("All convertKelvinToCelsius test cases passed")

# Test for Kelvin to Fahrenheit
def test_convertKelvinToFahrenheit():
    print("Testing convertKelvinToFahrenheit...")
    assert convertKelvinToFahrenheit(273.15) == 32.00, "Test case 1 failed"
    assert convertKelvinToFahrenheit(373.15) == 212.00, "Test case 2 failed"
    assert convertKelvinToFahrenheit(0.00) == -459.67, "Test case 3 failed"
    assert convertKelvinToFahrenheit(298.15) == 77.00, "Test case 4 failed"
    assert convertKelvinToFahrenheit(573.15) == 572.00, "Test case 5 failed"
    print("All convertKelvinToFahrenheit test cases passed")

# Run all tests
test_convertCelsiusToKelvin()
test_convertCelsiusToFahrenheit()
test_convertFahrenheitToCelsius()
test_convertFahrenheitToKelvin()
test_convertKelvinToCelsius()
test_convertKelvinToFahrenheit()

print("All tests passed.")
