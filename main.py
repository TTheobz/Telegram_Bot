import telebot as tb
import requests, json
from app import recuperar_detalhe_coletivo

chave = "SUA_CHAVE_AQUI"

bot = tb.TeleBot(chave)
def buscar_livro(mensagem):
  url="url_do_banco_de_dados"
  livros = requests.get(url)
  livros = livros.json()

  for book in livros:
    titulo = book["titulo"]
    autor = book["autor"]
    bot.send_message(mensagem.chat.id, f"{livros} --- {autor}")

def responder_start(mensagem):
	bot.send_message(mensagem.chat.id, "Ola, seja bem vindo ao chat do Theo_bz")
	bot.send_message(mensagem.chat.id, "comandos disponiveis:")
	bot.send_message(mensagem.chat.id, "/livro")
bot.polling()
