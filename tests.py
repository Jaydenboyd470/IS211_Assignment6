# tests.py
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

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

# Run tests
test_convertCelsiusToKelvin()
test_convertCelsiusToFahrenheit()
