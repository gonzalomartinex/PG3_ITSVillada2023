def roman_to_decimal(roman_number):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal_number = 0
    previous_value = 0
    roman_number = roman_number.upper()
    
    for char in reversed(roman_number):
        value = roman_values[char]

        if value < previous_value:
            decimal_number -= value
        else:
            decimal_number += value

        previous_value = value

    return decimal_number

def test_roman_to_decimal():
    # Casos de prueba válidos
    assert roman_to_decimal("I") == 1
    assert roman_to_decimal("IV") == 4
    assert roman_to_decimal("IX") == 9
    assert roman_to_decimal("LVIII") == 58
    assert roman_to_decimal("MCMXCIV") == 1994

    # Casos de prueba con letras en mayúscula y minúscula
    assert roman_to_decimal("iii") == 3
    assert roman_to_decimal("xlii") == 42

    # Caso de prueba con un número romano vacío
    assert roman_to_decimal("") == 0



    print("Todas las pruebas pasaron exitosamente.")

test_roman_to_decimal()
