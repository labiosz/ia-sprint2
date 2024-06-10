import openai
import json

def main():
    
  openai.api_key = 'sua_chave_api'

  pergunta = "Qual é o estado atual do estoque de medicamentos?"
  resposta = consultar_chatgpt(pergunta)

  if reposta:
     print("Resposta do chatGPT: ",resposta)
  else:
     print('Falha ao obter a API do chatGPT, verifique a chave')

if __name__ == __main__:
   main()


def consultar_chatgpt(pergunta):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=pergunta,
      max_tokens=100
    )
    return response.choices[0].text.strip()




