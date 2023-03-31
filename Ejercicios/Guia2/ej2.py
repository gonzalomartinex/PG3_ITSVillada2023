class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    
    def esta_regular(self):
        if self.nota >= 6:
            print("El alumno está regular.")
        else:
            print("El alumno no está regular.")


Alumno1 = Alumno("Marcos", 7)
Alumno1.mostrar_datos()
Alumno1.esta_regular()


Alumno2 = Alumno("Pepe", 4)
Alumno2.mostrar_datos()
Alumno2.esta_regular()
