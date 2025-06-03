import telebot as tb
import requests, json
from app import recuperar_detalhe_coletivo
                                                                   chave = "8119155152:AAGrH0QBrW0WwrM99oN0BaGFY-ckztucqec"

bot = tb.TeleBot(chave)

@bot.message_handler(commands=["github"])
def responder_perfil(mensagem):                                            bot.send_message(mensagem.chat.id, "Github: https://github.
com/AndreBezer")

@bot.message_handler(commands=["livros"])
def buscar_livro(mensagem):
    url = "http://127.0.0.1:5000/api/book"
    livros = requests.get(url)                                         livros = livros.json()

    for book in livros:
        titulo = book["titulo"]
        autor = book["autor"]
        bot.send_message(mensagem.chat.id, f"{titulo} --- {autor}")

@bot.message_handler(commands=["instagram"])
def responder_perfil(mensagem):                                            bot.send_message(mensagem.chat.id, "Instagram: https://www.
instagram.com/andrelbrj_?utm_source=qr&igsh=MTZndDBpd296NTJueQ==")

@bot.message_handler(commands=["linkedin"])
def responder_perfil(mensagem):                                            bot.send_message(mensagem.chat.id, "LinkedIn: https://www.l
inkedin.com/in/andr%C3%A9-luis-219009353/")                        
@bot.message_handler(commands=["start"])
def responder_start(mensagem):                                             bot.send_message(mensagem.chat.id, "Ola, seja bem vindo ao
chat do Andre Bezer")                                                      bot.send_message(mensagem.chat.id, "comandos disponiveis:")
        bot.send_message(mensagem.chat.id,
        """
        /instagram
        /linkedin
        /github
        /livros
        """)
bot.polling()