import mysql.connector

class ConexaoComOBancoDeDados:

  def conexao(self):
    mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234",
      database="agenda"
    )




