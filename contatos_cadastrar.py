import PySimpleGUI as sg
from banco.crud import FuncoesCrud

class CadastroDeContatos:

    def formulario_cadastro(self):
        sg.theme('TanBlue')
        layout = [
            [sg.Text('Nome:      ', text_color="#000000", font=('Arial', 10, 'bold')),sg.Input(key='input_nome')],
            [sg.Text('Endereço:',text_color="#000000", font=('Arial', 10, 'bold')),sg.Input(key='input_endereco')],
            [sg.Text('Telefone: ', text_color="#000000", font=('Arial', 10, 'bold')),    sg.Input(key='input_telefone')],
            [sg.Text('E-mail:     ', text_color="#000000", font=('Arial', 10, 'bold')), sg.Input(key='input_email')],
            [sg.Button('Salvar')]
            ]



        layout_principal = [[sg.Frame('Cadastro', layout)]]

        window = sg.Window('Cadastro de contatos', layout_principal).Finalize()


        while True:

            event, values = window.read()
            if event in (None, 'Close Window'):
                window.close()
                break



            if event == 'Salvar':
                nome = (values['input_nome'])
                endereco = values['input_endereco']
                telefone = values['input_telefone']
                email = values['input_email']

                # print(nome)
                # print(endereco)
                # print(telefone)
                # print(email)

                FuncoesCrud(nome=nome, endereco=endereco, telefone=telefone, email=email)
                FuncoesCrud.insert(self='0')
