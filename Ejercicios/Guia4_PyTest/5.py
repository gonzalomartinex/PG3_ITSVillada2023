def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False

def test_search_matrix():
    # Matriz de prueba
    matrix = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

    # Caso de prueba con número presente en la matriz
    assert search_matrix(matrix, 5) == True

    # Caso de prueba con número no presente en la matriz
    assert search_matrix(matrix, 10) == False

    # Caso de prueba con matriz vacía
    assert search_matrix([], 5) == False

    # Caso de prueba con matriz de una sola fila vacía
    assert search_matrix([[]], 5) == False

    print("Todas las pruebas pasaron exitosamente.")

test_search_matrix()
