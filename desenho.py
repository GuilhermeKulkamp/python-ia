'''

'''
import turtle
import math

# Configurações da tela
tela = turtle.Screen()
tela.setworldcoordinates(-300, -300, 300, 300)
tela.bgcolor("white")

# Criação da tartaruga para desenhar
desenhador = turtle.Turtle()
desenhador.speed(0)
desenhador.penup()

# Função para desenhar os eixos
def desenhar_eixos():
    desenhador.goto(-300, 0)
    desenhador.pendown()
    desenhador.goto(300, 0)
    desenhador.penup()
    desenhador.goto(0, -300)
    desenhador.pendown()
    desenhador.goto(0, 300)
    desenhador.penup()

# Função para desenhar a equação
def desenhar_equacao(equacao):
    desenhador.penup()
    desenhador.goto(-300, 0)

    for x in range(-300, 301):
        try:
            # Avalia a expressão para encontrar y
            y = eval(equacao.replace('x', str(x)))
            desenhador.goto(x, y)
            desenhador.pendown()
        except:
            desenhador.penup()  # Caso não seja possível calcular um ponto, a tartaruga para de desenhar

# Função principal
def main():
    # Desenhar os eixos cartesianos
    desenhar_eixos()

    # Entrada do usuário: equação em função de 'x'
    equacao = tela.textinput("Entrada de Equação", "Insira a equação em função de x (ex: x**2, 2*x + 3):")

    # Desenhar a equação fornecida
    desenhar_equacao(equacao)

    # Mantém a janela aberta
    tela.mainloop()

# Executa o programa principal
main()
