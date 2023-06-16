import pytest

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if any(char in "!@#$%^&*()_+-=[]{}|;':,.<>?/~`" for char in password):
        return False
    return True

def test_validate_password():
    # Casos de prueba válidos
    assert validate_password("Abcdefg1") == True
    assert validate_password("aB1") == False
    assert validate_password("Password123") == True

    # Casos de prueba inválidos
    assert validate_password("short") == False
    assert validate_password("Password") == False
    assert validate_password("12345678") == False
    assert validate_password("Abcdefg!") == False

    # Casos de prueba con contraseñas vacías
    assert validate_password("") == False

    # Casos de prueba con contraseñas que solo contienen letras
    assert validate_password("abcdefgh") == False
    assert validate_password("ABCDEFGH") == False

    # Casos de prueba con contraseñas que solo contienen números
    assert validate_password("12345678") == False
    assert validate_password("987654321") == False

    # Caso de prueba con caracteres especiales
    assert validate_password("Abcdefg1!") == False
    assert validate_password("!Password123") == False

    print("Todas las pruebas pasaron exitosamente.")

test_validate_password()
