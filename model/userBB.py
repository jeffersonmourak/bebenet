#user.py

class UserModelBB(object):
    
    def __init__(self, cpf, nome, idade, nFilhos, login, senha):
        self.cpf = cpf
        self.idade = idade
        self.nFilhos = nFilhos
        self.login = login
        self.senha = senha
