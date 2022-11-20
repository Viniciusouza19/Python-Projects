import tkinter
import requests
from tkinter import *


def fazer_requisicao():
    moedaEntrada = enntry_moeda_entrada.get()
    moedaSaida = enntry_moeda_saida.get()
    valorEntrada = enntry_valor.get()
    if moedaEntrada == '':
        textoResposta["text"] = 'Digite a moeda de ENTRADA'

    elif moedaSaida == '':
        textoResposta["text"] = 'Digite a moeda de SAIDA'
    elif valorEntrada == '':
        textoResposta["text"] = 'Digite o VALOR a ser convertido'
    elif valorEntrada == '0':
        textoResposta["text"] = 'Digite um valor maior que 0'
    elif moedaEntrada == moedaSaida:
        textoResposta["text"] = 'Entrada e Saida iguais!!!'

    else:
        requisicao = requests.get(
            f"https://economia.awesomeapi.com.br/all/{moedaEntrada.upper()}-{moedaSaida.upper()}")
        if requisicao.status_code == 200:
            calc = float(requisicao.json()[
                         f"{moedaEntrada.upper()}"]['bid'])*float(valorEntrada)

            textoResposta['text'] = f"Conversao: \n{valorEntrada} {moedaEntrada.upper()} = {calc:.2f} {moedaSaida.upper()}"
        else:
            # textoResposta.config(font='Moeda não encontrada')
            textoResposta['text'] = f"Erro {requisicao.status_code}"


def placeholderEntrada(event):
    if len(event) > 0:
        enntry_moeda_entrada_placeholder.config(text='')
        enntry_moeda_entrada_placeholder.place_configure(x=4000)
    else:
        enntry_moeda_entrada_placeholder.config(text='Moeda de Entrada')
        enntry_moeda_entrada_placeholder.place_configure(x=100, y=14)


def placeholderSaida(event):
    if len(event) > 0:
        enntry_moeda_saida_placeholder.config(text='')
        enntry_moeda_saida_placeholder.place_configure(x=4000)
    else:
        enntry_moeda_saida_placeholder.config(text='Moeda de Saida')
        enntry_moeda_saida_placeholder.place_configure(x=110, y=70)


def placeholderValor(event):
    if len(event) > 0:
        enntry_valor_placeholder.config(text='')
        enntry_valor_placeholder.place_configure(x=4000)
    else:
        enntry_valor_placeholder.config(text='Valor')
        enntry_valor_placeholder.place_configure(x=86, y=122)


janela = Tk()
janela.title("Cambio de Moedas")
janela.geometry("360x300")
entry_frames = tkinter.Frame(janela, height=300)


# Entrada de Moeda
enntry_moeda_entrada = Entry(entry_frames, width=26, font=('Arial', 18))
enntry_moeda_entrada.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
enntry_moeda_entrada.bind(
    "<KeyRelease>", lambda event: placeholderEntrada(enntry_moeda_entrada.get()))

enntry_moeda_entrada_placeholder = Label(
    entry_frames, text="Moeda de Entrada", fg="grey", font=("Bold", 13), bg="white")
enntry_moeda_entrada_placeholder.place(x=100, y=14)
enntry_moeda_entrada_placeholder.bind(
    "<Button-1>", lambda event: enntry_moeda_entrada.focus())


# Moeda de Saida
enntry_moeda_saida = Entry(entry_frames, width=26, font=('Arial', 18))
enntry_moeda_saida.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
enntry_moeda_saida.bind(
    "<KeyRelease>", lambda event: placeholderSaida(enntry_moeda_saida.get()))

enntry_moeda_saida_placeholder = Label(
    entry_frames, text="Moeda de Saida", fg="grey", font=("Bold", 13), bg="white")
enntry_moeda_saida_placeholder.place(x=110, y=70)
enntry_moeda_saida_placeholder.bind(
    "<Button-1>", lambda event: enntry_moeda_saida.focus())


# Valor
enntry_valor = Entry(entry_frames, width=26, font=('Arial', 18))
enntry_valor.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
enntry_valor.bind(
    "<KeyRelease>", lambda event: placeholderValor(enntry_valor.get()))

enntry_valor_placeholder = Label(
    entry_frames, text="Valor a ser convertido", fg="grey", font=("Bold", 13), bg="white")
enntry_valor_placeholder.place(x=86, y=122)
enntry_valor_placeholder.bind("<Button-1>", lambda event: enntry_valor.focus())

# Resposta da conversao
boxResposta = Frame(entry_frames, width=250, height=60,
                    bg="White", borderwidth=1, relief="solid")
boxResposta.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
textoResposta = Label(entry_frames, text="Resposta",
                      font=("Bold", 10), fg="red", bg="white")
textoResposta.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


buttonConversao = Button(entry_frames, text="Converter",
                         command=fazer_requisicao, width=20, height=2, border=1)
buttonConversao.grid(row=4, column=0, columnspan=2)

entry_frames.pack(pady=14)
janela.mainloop()
