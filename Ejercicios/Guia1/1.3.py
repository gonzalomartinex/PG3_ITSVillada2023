def pintameee(alto,ancho,caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end=' ')
        print()

alto = int(input("Ingresa la altura del rectángulo: "))
ancho = int(input("Ingresa el ancho del rectángulo: "))
caracter = input("Ingresa el carácter a utilizar en el dibujo: ")

pintameee(alto,ancho,caracter)
