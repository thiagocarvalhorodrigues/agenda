from banco.db import ConexaoComOBancoDeDados


class FuncoesCrud:
    def __init__(self,nome,endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.cursor = ConexaoComOBancoDeDados.conexao(self='0')
        print('Inicializar',self.nome)




    def select(self):
        sql = ('SELECT nome, FROM cadastro')
        self.cursor.execute(sql)


    def insert(self):
        print('insert')
        print('dentro do insert')
        print(self.nome)

        sql_insert = "INSERT INTO cadastro (nome, endereco, telefone, email) VALUES (%s,%s,%s,%s)"
        valores = self.nome, self.endereco, self.telefone, self.email
        self.cursor.execute(sql_insert, valores)
        self.cursor.commit()


    def update(self):
        pass


    def delete(self):
        pass
