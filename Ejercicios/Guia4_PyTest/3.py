def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def test_is_anagram():
    # Casos de prueba válidos
    assert is_anagram("listen", "silent") == True
    assert is_anagram("debit card", "bad credit") == True

    # Casos de prueba con palabras que no son anagramas
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

    # Casos de prueba con mayúsculas y minúsculas
    assert is_anagram("Listen", "silent") == True
    assert is_anagram("Debit Card", "Bad Credit") == True

    # Casos de prueba con espacios y caracteres especiales
    assert is_anagram("eleven plus two", "twelve plus one") == True
    assert is_anagram("iceman", "cinema") == True

    print("Todas las pruebas pasaron exitosamente.")

test_is_anagram()
