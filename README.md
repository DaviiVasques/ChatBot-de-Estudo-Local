# 🤖 ChatBot de Estudo em Python (com Base de Conhecimento Local)

## 📚 Descrição

Este projeto é um **chatbot educacional local**, construído em Python puro, que responde dúvidas sobre Python com base em uma **base de conhecimento armazenada em JSON**. Ele simula uma conversa no terminal e é útil para revisar conteúdos de forma prática e rápida.

O projeto foi estruturado com **Programação Orientada a Objetos (POO)**, visando modularidade, clareza e facilidade de expansão.

---

## ✅ Funcionalidades

- Recebe perguntas do usuário via terminal
- Faz busca por palavras-chave na base de conhecimento
- Retorna respostas explicativas sobre listas, dicionários, POO, loops, etc.
- Usa JSON como banco de dados leve e local
- Pode ser facilmente expandido com novos tópicos

---

## 🧱 Estrutura do Projeto

chatbot_estudo/

├── main.py # Script principal que inicia o bot

├── core/
│ ├── init.py # Torna a pasta um pacote
│ └── bot.py # Contém a classe BotEstudo com a lógica principal

├── knowledge/
│ └── base_respostas.json # Base de conhecimento do bot (em formato chave/valor)
