import tkinter as tk
from tkinter import scrolledtext
# import re

class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mensagens em Markdown")
        self.geometry("500x600")

        # Campo de entrada da mensagem
        self.caixa_texto = tk.Text(self, height=5, width=50)
        self.caixa_texto.pack(padx=10, pady=10)

        # Botão enviar
        self.botao_enviar = tk.Button(self, text="Enviar", 
command=self.enviar_mensagem)
        self.botao_enviar.pack(pady=10)

        # Seção de saída das mensagens (com scroll)
        self.secao_saida = scrolledtext.ScrolledText(self, height=20, 
width=50)
        self.secao_saida.pack(padx=10, pady=10)

        # Botão para sair da aplicação
        self.botao_sair = tk.Button(self, text="Sair", command=self.sair)
        self.botao_sair.pack(pady=10)

    def enviar_mensagem(self):
        mensagem = self.caixa_texto.get("1.0", "end-1c")
#        if re.match(r"^[A-Za-z0-9\s\#]+$", mensagem): # regex para verificar se a msg é em markdown
        self.secao_saida.insert(tk.END, f"> {mensagem}\n\n") # insere a msg no campo de saída
        self.caixa_texto.delete("1.0", tk.END) # limpa o campo de entrada
#        else:
#            print("Mensagem inválida")

    def sair(self):
        self.destroy()

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()