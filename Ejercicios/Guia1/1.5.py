def Palindromos(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

MiPalabra = input("Ingresa una palabra: ")
print(Palindromos(MiPalabra))

