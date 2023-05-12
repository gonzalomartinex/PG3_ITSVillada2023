def sumar_numeros():
    while True:
        try:
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            resultado = num1 + num2
            return resultado
        except ValueError:
            print("No estas poniendo un numero entero o estas poniendo un valor invalido. Intente de vuelta")

print(sumar_numeros())
