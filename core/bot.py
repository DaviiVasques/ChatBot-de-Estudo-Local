import json

class BotEstudo:
    def __init__(self, base_conhecimento_path):
        self.base_conhecimento_path = base_conhecimento_path
        self.respostas = self.carregar_base()

    def carregar_base(self):
        try:
            with open(self.base_conhecimento_path, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print("❌ Base de conhecimento não encontrada.")
            return {}
        except json.JSONDecodeError:
            print("❌ Erro ao ler o arquivo JSON.")
            return {}

    def responder(self, pergunta):
        pergunta = pergunta.lower()

        for chave in self.respostas:
            if chave in pergunta:
                return self.respostas[chave]

        return "Ainda não sei responder isso. Que tal pesquisar mais sobre o assunto e me ensinar depois?"
