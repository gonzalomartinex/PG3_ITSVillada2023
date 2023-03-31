class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        
    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.padre}\nMadre: {self.madre}\nHijos: {hijos_str}"

familia1 = Familia("Juan", "María", ["Pedro", "Ana", "Luis"])
print(familia1)
