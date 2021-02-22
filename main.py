import PySimpleGUI as sg
from contatos_cadastrar import CadastroDeContatos
from listar import ListaTodosCadastrados


class Inicial:

    sg.theme('TanBlue')
    background_fundo = '#FF4500'
    background_fonte = '#FFFAFA'


    layout = [
        [sg.Text('Agenda Telefônica',text_color="#000000", font=('Arial', 10, 'bold'))],
        [sg.Button('Listar Contatos',button_color=(background_fonte,background_fundo), key='listar_contatos')],
        [sg.Button('Adicionar Contatos',button_color=(background_fonte,background_fundo), key='adicionar_contatos')],
        [sg.Button('Alterar Contatos', button_color=(background_fonte, background_fundo), key='adicionar_contatos')],
        [sg.Button('Excluir Contatos', button_color=(background_fonte, background_fundo), key='adicionar_contatos')]]

    layout_principal = [[sg.Frame('Agenda',layout)]]

    window = sg.Window('Agenda', layout_principal).Finalize()



    while True:

        event, values = window.read()
        if event in (None, 'Close Window'):


            window.close()
            break


        if event == 'listar_contatos':
            ListaTodosCadastrados.formulario_para_listar_todos_cadastrados(self='0')




        if event == 'adicionar_contatos':
           CadastroDeContatos.formulario_cadastro(self='0')








