import PySimpleGUI as sg
from banco.db import ConexaoComOBancoDeDados


class ListaTodosCadastrados:

    def formulario_para_listar_todos_cadastrados(self):
        sg.theme('TanBlue')
        layout = [
            [sg.Button('Nome')],

            ]

        layout_principal = [[sg.Frame('Lista dos Contatos Cadastrados', layout)]]

        window = sg.Window('Lista dos Contatos Cadastrados', layout_principal).Finalize()

        while True:

            event, values = window.read()
            if event in (None, 'Close Window'):
                window.close()
                break

            if event == 'Nome':
                ConexaoComOBancoDeDados.select(self='0')




