import openai

openai.api_key = 'sua_chave_api'

def consultar_chatgpt(pergunta):
  try:    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=pergunta,        max_tokens=100
      )
    return response.choices[0].text.strip()
  except Exception as e:
    logging.error(f'Erro ao acessar a API da OpenAI: {e}')
    return "Desculpe, ocorreu um erro ao processar sua solicitação"

# Exemplo de uso
pergunta = "Qual é o estado atual do estoque de medicamentos?"
resposta = consultar_chatgpt(pergunta)
print(resposta)
