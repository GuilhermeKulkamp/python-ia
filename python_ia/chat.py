# Importar as bibliotecas
# abrir uma seção de chat
    # manter a seção ativa
        # pegar a pergunta do usuário
            # Se for "/bye" encerrar seção
        # fazer a pergunta a IA
        # pegar a resposta da IA
        # acrescentar pergunta e resposta ao arquivo de seção 


import ollama

texto = input('pergunta: ')
stream = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': texto}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)