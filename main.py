import PySimpleGUI as sg

sg.theme('TanBlue')
background_fundo = '#FF4500'
background_fonte = '#FFFAFA'


layout =    [[sg.Text('Agenda Telefônica',text_color="#000000", font=('Arial', 10, 'bold'))],
            [sg.Button('Listar Contatos',button_color=(background_fonte,background_fundo), key='listar_contatos')],
            [sg.Button('Adicionar Contatos',button_color=(background_fonte,background_fundo), key='adicionar_contatos')],


            ]

layout_principal = [
        [sg.Frame('Agenda',layout)]
    ]

window = sg.Window('Agenda', layout_principal).Finalize()
    

while True:

    event, values = window.read()
    if event in (None, 'Close Window'):


        window.close()
        break








