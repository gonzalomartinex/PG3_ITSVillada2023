import math

def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        raise ValueError("La lista de números está vacía")

    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_deviation = math.sqrt(variance)

    return mean, std_deviation

def test_calculate_statistics():
    # Caso de prueba con una lista de números
    numbers = [1, 2, 3, 4, 5]
    mean, std_deviation = calculate_statistics(numbers)
    assert mean == 3.0

    print("Todas las pruebas pasaron exitosamente.")

test_calculate_statistics()
