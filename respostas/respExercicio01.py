class Aluno:
    def __init__ (self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
class Disciplina:
    def __init__ (self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        
A1 = Aluno("Maria", 123456789, "Matemática")
A2 = Aluno("João", 987654321, "Geografia")
D1 = Disciplina("Matemática", 1, 24)
D2 = Disciplina("Geografia", 2, 12)

