from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.json
    # Supondo que `dados` contém as informações necessárias para a previsão
    previsao = model.predict(dados)
    return jsonify({'previsao': previsao.tolist()})

@app.route('/consultar', methods=['POST'])
def consultar():
    dados = request.json
    pergunta = dados['pergunta']
    resposta = consultar_chatgpt(pergunta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
