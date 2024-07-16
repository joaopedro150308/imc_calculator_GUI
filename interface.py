import PySimpleGUI as sg

def iniciar_interface():
    # Tema
    sg.theme('DarkGray8')
    # Layout
    layout = [
        [sg.Text('Peso(Kg)', size=(10, 1)), sg.Input(key='peso', size=(8, 1))],
        [sg.Text('Altura(m)', size=(10, 1)), sg.Input(key='altura', size=(8, 1))],
        [sg.Text('IMC', size=(10, 1), visible=False, key='texto_imc'), sg.Input(default_text=None, key='imc', size=(
            5, 1), readonly=True, disabled_readonly_background_color='#32414B', visible=False)],
        [sg.Text('Categoria', size=(10, 1), visible=False, key='texto_categoria'), sg.Input(
            key='categoria', size=(15, 1), visible=False, readonly=True, disabled_readonly_background_color='#32414B')],
        [sg.Button('Calcular'), sg.Button('Sair')]
    ]
    # Janela
    window = sg.Window('Calculadora de IMC', layout=layout, finalize=True)
    # Tratamento de eventos
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        elif event == 'Calcular':
            peso = float(value['peso'])
            altura = float(value['altura'])
            
            # Calculando imc
            from imc import calcular_imc
            imc = calcular_imc(peso, altura)

            # Encontrando a categoria de acordo com aquele IMC
            from categorias import encontrar_categoria
            categoria = encontrar_categoria(imc)

            # Definindo atualizações do layout após apertar o botão
            window['texto_imc'].update(visible=True)
            window['imc'].update(value=f'{imc:.1f}', visible=True)
            window['texto_categoria'].update(visible=True)
            window['categoria'].update(visible=True, value=categoria.estado, text_color=categoria.text_color)
