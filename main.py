import telebot as tb
import requests, json
from app import recuperar_detalhe_coletivo
chave = "_sua_chave_"

bot = tb.TeleBot(chave)

@bot.message_handler(commands=["livros"])
def buscar_livro(mensagem):
    url = "http://127.0.0.1:5000/api/book"
    livros = requests.get(url)                                        
    livros = livros.json()

    for book in livros:
        titulo = book["titulo"]
        autor = book["autor"]
        bot.send_message(mensagem.chat.id, f"{titulo} --- {autor}")
                  
@bot.message_handler(commands=["start"])
def responder_start(mensagem):                                             
  bot.send_message(mensagem.chat.id, "Ola, seja bem vindo ao chat do Andre Bezer")                                                      
bot.send_message(mensagem.chat.id, "comandos disponiveis:")
        bot.send_message(mensagem.chat.id,
        """
        /livros
        """)
bot.polling()
