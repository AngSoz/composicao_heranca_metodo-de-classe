class Registrar: 
    def __init__(self, tipo, data):
        self.titulo = tipo
        self.ano = data

        
    def get_resito(self):
        return f"{self.tipo}, {self.data}"
    
    @classmethod
    def saque(cls, tipo, data):
        return cls(tipo, data)
    
    @staticmethod
    def imprimi_extrato():
        print("imprindo...")
    
    #singleton
        

print(Registrar.saque("Saque", "04/07/2026").__dict__)
print(Registrar.imprimi_extrato())