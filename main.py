from core.bot import BotEstudo

def iniciar_bot():
    bot = BotEstudo("knowledge/base_respostas.json")
    print("🤖 Bot de Estudo de Python")
    print("Digite sua pergunta ou 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Bot: Até logo! Continue estudando 😉")
            break
        resposta = bot.responder(pergunta)
        print("Bot:", resposta)

if __name__ == "__main__":
    iniciar_bot()
