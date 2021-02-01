from tinydb import TinyDB, Query

class BancodeDados:
     banco = TinyDB('banco/profile.json')
     caminho_profile = 'banco_profile/profile.json'
     User = Query()

     def __init__(self,numero_):
          self.numero_da_conta = numero_da_conta


     def insert(self):

          self.banco.insert({'contato':'INSERIR VALOR')})

     def select_all(self):
          return self.banco.all()

     def delete(self):

          return self.banco.remove(BancodeDados.User.celular == 'INSERIR VALOR')