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

Para adicionar botões no programa que permitem fechar o aplicativo e inserir uma nova fórmula, podemos utilizar a funcionalidade de eventos do `turtle` em combinação com a manipulação de funções de fechamento e reinicialização do gráfico.

Aqui está o código atualizado:

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

# Função para limpar a tela e permitir a inserção de uma nova equação
def nova_equacao():
    desenhador.clear()  # Limpa o desenho anterior
    desenhar_eixos()    # Desenha os eixos novamente
    equacao = tela.textinput("Entrada de Equação", "Insira a equação em função de x (ex: x**2, 2*x + 3):")
    desenhar_equacao(equacao)

# Função para fechar o programa
def fechar_programa():
    tela.bye()

# Função principal
def main():
    # Desenhar os eixos cartesianos
    desenhar_eixos()

    # Entrada do usuário: equação em função de 'x'
    equacao = tela.textinput("Entrada de Equação", "Insira a equação em função de x (ex: x**2, 2*x + 3):")

    # Desenhar a equação fornecida
    desenhar_equacao(equacao)

    # Criar botões na tela para fechar o programa e inserir uma nova equação
    turtle.listen()
    turtle.onkey(nova_equacao, "n")  # Aperte 'n' para nova equação
    turtle.onkey(fechar_programa, "q")  # Aperte 'q' para sair do programa

    # Mensagem de instrução na tela
    turtle.penup()
    turtle.goto(-290, 270)
    turtle.write("Pressione 'n' para nova equação, 'q' para sair.", font=("Arial", 10, "normal"))

    # Mantém a janela aberta
    tela.mainloop()

# Executa o programa principal
main()
```

### Explicação das Novas Funcionalidades:

1. **Botões de Nova Equação e Fechar Programa:**
   - O comando `turtle.onkey(nova_equacao, "n")` configura a tecla `n` para que o usuário possa inserir uma nova equação. Quando a tecla é pressionada, a tela é limpa e o programa solicita uma nova fórmula.
   - O comando `turtle.onkey(fechar_programa, "q")` configura a tecla `q` para fechar a janela e encerrar o programa. Quando o usuário aperta `q`, o comando `tela.bye()` é executado para fechar a janela Turtle.

2. **Exibição de Instruções:**
   - Adicionei uma mensagem na parte superior da tela informando ao usuário que ele pode pressionar as teclas `n` para uma nova equação e `q` para sair.

3. **Manter o Programa Aberto:**
   - A função `tela.mainloop()` garante que o programa continue rodando até que o usuário feche a janela ou pressione `q` para sair.

### Resumo das Teclas de Atalho:

- **`n`**: Para inserir uma nova equação.
- **`q`**: Para fechar o programa.