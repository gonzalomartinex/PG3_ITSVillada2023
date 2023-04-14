def contar_vocales(frase):
    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra.lower() in vocales:
            contador += 1

    return contador

print(contar_vocales("Hola me llamo Gonzalo"))
