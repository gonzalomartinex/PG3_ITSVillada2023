while True:
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    num_mes = input("Ingrese el número de mes (1-12): ")

    try:
        indice_mes = int(num_mes) - 1
        nombre_mes = meses[indice_mes]
        print("El nombre del mes es:", nombre_mes)
        
    except IndexError:
        print("El número de mes ingresado no es válido, Ingresa in numero entre el 1 y el 12.")
