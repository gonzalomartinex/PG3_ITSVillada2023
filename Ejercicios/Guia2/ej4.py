class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    
    def suma(self):
        print("La suma es:", self.num1 + self.num2)
    
    def resta(self):
        print("La resta es:", self.num1 - self.num2)
    
    def multiplicacion(self):
        print("La multiplicación es:", self.num1 * self.num2)
    
    def division(self):
        if self.num2 == 0:
            print("Infinito")
        else:
            print("La división es:", self.num1 / self.num2)


operaciones1 = Operaciones(6, 5)
