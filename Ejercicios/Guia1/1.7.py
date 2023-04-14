def numero_step(numero):
    # Convertir el número en una cadena de texto
    numero_str = str(numero)
    # Verificar si la diferencia entre cada par de dígitos consecutivos es 1 utilizando slicing
    es_step = all(abs(int(numero_str[i]) - int(numero_str[i+1])) == 1 for i in range(len(numero_str) - 1))
    return es_step


print(numero_step(123234))
print(numero_step(1234567890)) 
print(numero_step(9876787654))
