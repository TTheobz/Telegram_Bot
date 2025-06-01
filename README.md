.

📌 Visão Geral
O bot oferece dois comandos principais:

/start → Mensagem de boas-vindas e lista de comandos.

/livro → Exibe todos os livros cadastrados no banco de dados no formato:
"titulo --- autor".

⚙️ Configuração
Pré-requisitos
Python 3.x

Bibliotecas:

bash
pip install pyTelegramBotAPI requests
Variáveis de Ambiente
chave: Token do bot do Telegram (obtido via @BotFather).

url: Endpoint da API que retorna os livros (ex: http://localhost:5000/api/book).

📋 Estrutura do Código
1. Função responder_start(mensagem)
O que faz?

Envia uma mensagem de boas-vindas.

Lista os comandos disponíveis (/livro).

Fluxo:

plaintext
Usuário → /start → Bot → "Olá, seja bem-vindo..."  
2. Função buscar_livro(mensagem)
O que faz?

Faz uma requisição GET para a API de livros.

Formata a resposta em "titulo --- autor".

Envia cada livro como uma mensagem separada no chat.

Fluxo:

plaintext
Usuário → /livro → Bot → Requisição à API → Exibe livros  
Tratamento de Erros (Recomendado):

Se a API não responder, exibir: "Erro ao carregar livros. Tente mais tarde.".

Se não houver livros, exibir: "Nenhum livro cadastrado.".

🚀 Como Executar
Inicie a API de livros (app.py):

bash
python app.py
Rode o bot (bot.py):

bash
python bot.py
---
📄 Exemplo de Saída
Comando /livro
plaintext
Dom Casmurro --- Machado de Assis  
1984 --- George Orwell  
