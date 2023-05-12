while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
        
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        
    except ValueError:
        print("Los valores ingresados no son numéricos.")
