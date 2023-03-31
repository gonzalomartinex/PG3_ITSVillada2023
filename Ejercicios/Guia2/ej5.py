class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def cargar(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)
        if self.sueldo > 3000:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")


persona1 = Persona("Juan", 25)
persona1.imprimir()


empleado1 = Empleado("Pedro", 35, 4000)
empleado1.imprimir()
