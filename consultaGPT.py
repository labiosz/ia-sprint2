import openai

openai.api_key = 'sua_chave_api'

def consultar_chatgpt(pergunta):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=pergunta,
      max_tokens=100
    )
    return response.choices[0].text.strip()

# Exemplo de uso
pergunta = "Qual é o estado atual do estoque de medicamentos?"
resposta = consultar_chatgpt(pergunta)
print(resposta)
