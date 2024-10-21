Para criar um programa em Python que desenha equações matemáticas usando o módulo `turtle`, precisaremos combinar a funcionalidade de desenhar no plano cartesiano e a avaliação de expressões matemáticas inseridas pelo usuário. 

Aqui está um exemplo de código:

```python
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
```

### Como o programa funciona:

1. **Eixos Cartesianos:** A função `desenhar_eixos()` desenha os eixos x e y no plano usando a tartaruga.
2. **Entrada do Usuário:** A função `tela.textinput()` coleta uma equação matemática em termos de `x`, que o usuário insere, como por exemplo: `x**2`, `2*x + 3`, ou `math.sin(x)`.
3. **Desenho da Equação:** A função `desenhar_equacao()` percorre valores de `x` de -300 a 300 e calcula o valor de `y` correspondente usando a função `eval()` para avaliar a expressão fornecida.
4. **Tratamento de Erros:** Se houver erros de cálculo (como divisão por zero ou valores indefinidos), o código simplesmente "levanta" a caneta, evitando desenhar nesse ponto.

### Exemplos de equações que podem ser inseridas no aplicativo:

- `x**2` (parábola quadrática)
- `2*x + 3` (linha reta)
- `math.sin(x)` (função seno)
- `math.cos(x)` (função cosseno)
- `math.tan(x)` (função tangente)
- `x**3 - 4*x` (cúbica)

Essas equações devem estar em termos de `x`, e o usuário pode utilizar operações básicas e funções da biblioteca `math`.

