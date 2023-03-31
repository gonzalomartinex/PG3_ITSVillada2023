class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)



persona1 = Persona("pepe")

persona1.mostrar_nombre()

persona2 = Persona("marcos")

persona2.mostrar_nombre()