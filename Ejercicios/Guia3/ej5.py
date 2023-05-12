try:
    archivo = open("ejemplo.txt", "w")

    archivo.write("Hola\n")
    archivo.write("Esto es una prueba\n")
    archivo.write("Adiós\n")
    
    # entero
    archivo.write(1)
    
    archivo.close()

except TypeError:
    print("No se puede escribir un entero en el archivo de texto.")
