def es_bisiesto(año):
    """
    Determina si un año es bisiesto o no
    """
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False

año = int(input("Introduzca un año: "))
if es_bisiesto(año):
    print(año, "es bisiesto")
else:
    print(año, "no es bisiesto")
