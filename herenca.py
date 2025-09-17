class Pessoa:
    def __init__(self, nome, cpf, tipo_sangue):
        self.nome = nome
        self.cpf = cpf
        self.tipo_sangue = tipo_sangue
        
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}"
    
    def dormir(self):
        return f"Eu estou dormindo {self.nome}"
    
class Mestre:
    def __init__(self, titulo):
        self.titulo = titulo
    
    
class Professor(Pessoa, Mestre):
    def __init__(self, nome, cpf, titulo, turma, tipo_sangue, ):
        super().__init__(nome, cpf, tipo_sangue)
        Mestre.__init__(self, titulo)
        self.turma = turma
        
class Aluno(Pessoa): 
    def __init__(self, nome, cpf, nota, tipo_sangue):
        super().__init__(nome, cpf, tipo_sangue)
        self.nota = nota
        
class Inpector(Pessoa):
    def __init__(self, nome, cpf, turno, tipo_sangue):
        super().__init__(nome, cpf, tipo_sangue)
        self.turno = turno 
        

prof = Professor("joão", "123", "Turma 33", "A+", "Dr")
print(prof.apresentar())
print(prof.dormir())


