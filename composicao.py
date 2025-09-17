
class Dependente: 
    def __init__(self, nome_d, sobrenome, parentesco):
        self.nome_d = nome_d 
        self.sobrenome = sobrenome 
        self.parentesco = parentesco
        
    def __str__(self):
        return self.nome_d
        
class Funcionario:
    
    def __init__(self, nome, sobrenome, idade, cpf, endereco, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.dependentes = []
        
    def add_dependente(self, nome_d, sobrenome, parentesco): 
        dependente = Dependente(nome_d, sobrenome, parentesco)
        self.dependentes.append(dependente)
        # print(f"Dependente adicionado: {nome_d} {sobrenome} - grau: {parentesco}")
        
    def listar_dependente(self):
        
        nome_dep = f"Denpendentes:  "
        for dep in self.dependentes:
            nome_dep += f"{dep}, "
            
        return nome_dep
        

fun_1 = Funcionario("João", "Lopes", 20, "12345", "R. xpt, 4", 14.000)

dep_1 = fun_1.add_dependente("Maria", "Lopes", "filha")
dep_2 = fun_1.add_dependente("Cida", "Lopes", "esposa")

print("\nFuncionario e seus dependentes")
print(fun_1.listar_dependente())