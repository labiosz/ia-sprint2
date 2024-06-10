from flask import Flask, request, jsonify
from consultaGPT import consultar_chatgpt 
import numpy as np
import modeloLSTM

app = Flask(__name__)

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json(force=True)
    # Supondo que `dados` contém as informações necessárias para a previsão
    if not dados:
        return jsonify({'Erro': 'Nenhum dado fornecido'}), 400
    try:    
        previsao = model.predict(dados)
        return jsonify({'previsao': previsao.tolist()})
    except Exception as e:
        return jsonify({'Erro' : str(e)}), 500
    
        
@app.route('/consultar', methods=['POST'])
def consultar():
    dados = request.get_json(force=True)
    if 'pergunta' not in dados:
        return jsonify({'Erro' : 'Campo "pergunta" é necessário'}), 400
    try:
        resposta = consultar_chatgpt(dados['pergunta'])
        return jsonify({'resposta' : resposta})
    except:
        return jsonify({'Erro' : str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
