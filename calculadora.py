import flet as ft
from flet import colors

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window.resizable = False
    page.window.width = 270
    page.window.height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True

    result = ft.Text(value='0', color=colors.WHITE, size=20)
    last_operator = {'value': ''}
    current_expression = {'value': ''}

    def calculate(expression):
        try:
            return str(eval(expression))
        except:
            return 'Error'

    def select(e):
        nonlocal current_expression
        value = e.control.content.value

        if value.isdigit() or value == '.':
            if result.value in ('0', 'Error'):
                current_expression['value'] = ''
            current_expression['value'] += value
            result.value = current_expression['value']
        elif value == 'AC':
            current_expression['value'] = ''
            last_operator['value'] = ''
            result.value = '0'
        elif value in ('/', '*', '-', '+'):
            if current_expression['value'] and current_expression['value'][-1] in ('/', '*', '-', '+'):
                current_expression['value'] = current_expression['value'][:-1]
            if result.value not in ('Error', '0'):
                last_operator['value'] = value
                current_expression['value'] += value
            result.value = current_expression['value']
        elif value == '=':
            if current_expression['value']:
                result.value = calculate(current_expression['value'])
                current_expression['value'] = result.value
        elif value == '%':
            if current_expression['value']:
                # Primeiramente, resolver a expressão para garantir que os valores numéricos sejam extraídos corretamente
                try:
                    result_value = float(calculate(current_expression['value']))
                    result.value = str(result_value * 0.01)  # Calcular o percentual
                    current_expression['value'] = result.value
                except:
                    result.value = 'Error'
                    current_expression['value'] = 'Error'
        elif value == '±':
            if current_expression['value']:
                if current_expression['value'].startswith('-'):
                    current_expression['value'] = current_expression['value'][1:]
                else:
                    current_expression['value'] = '-' + current_expression['value']
                result.value = current_expression['value']

        result.update()

    display = ft.Row(
        width=270,
        controls=[result],
        alignment='end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in botoes]

    keybord = ft.Row(
        width=270,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keybord)

ft.app(target=main)