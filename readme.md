
# Objetivo Principal

## Apresentação da Versão Beta:
Implementação das principais funcionalidades da proposta, incluindo previsão de desabastecimento de medicamentos e integração com uma API de IA (ChatGPT) para fornecer insights e recomendações.

## Objetivos Específicos
- Etapa Atual VS Proposta Inicial:

    Estamos iniciando o desenvolvimento das IAs.

- Frameworks/Bibliotecas Python, APIs e Ferramentas Utilizadas:

    ### Frameworks/Bibliotecas Python:

    #### Pandas:
    Utilizado para manipulação e análise de dados.
    
    #### NumPy: 
    Utilizado para operações numéricas e manipulação de arrays.
    
    #### TensorFlow/Keras: 
    Utilizado para construção e treinamento de modelos de deep learning.
    
    #### Scikit-learn: 
    Utilizado para pré-processamento de dados e validação de modelos.
    
    ---
    
    ### APIs:

    #### OpenAI API (ChatGPT): 
    Utilizada para fornecer insights contextuais sobre o estado do estoque e recomendações.

    ---
    
    ### Ferramentas/Plataformas:

    #### Jupyter Notebook: 
    Utilizado para desenvolvimento e experimentação com código Python.
    
    #### Flask: 
    Utilizado para criar uma API web que interage com o modelo de previsão e o ChatGPT.
    
    #### Git/GitHub: 
    Utilizado para controle de versão e colaboração no código-fonte.
    
    #### Docker: 
    Utilizado para criar containers que garantem a consistência do ambiente de desenvolvimento e produção.

    ---

- Recursos/Ferramentas dentro da aplicação:
    ### Pandas e NumPy:

    #### Manipulação de Dados: 
    Pandas e NumPy são utilizados para carregar, limpar, normalizar e manipular os dados de movimentação de estoque.
    Exemplo: Carregar os dados históricos de movimentação de estoque, preencher valores ausentes e normalizar os dados para serem utilizados pelo modelo.

    ---

    ### TensorFlow/Keras:

    #### Modelagem de Previsão: 
        
    Utilizado para construir e treinar um modelo LSTM que prevê a demanda futura de medicamentos com base nos dados históricos.
    Exemplo: Construir um modelo LSTM, treinar com os dados históricos e fazer previsões de desabastecimento.
        
    ---

    ### OpenAI API (ChatGPT):

    #### Insights e Recomendações: 
    Utilizado para responder perguntas em linguagem natural sobre o estado do estoque e fornecer recomendações baseadas nas previsões.
    Exemplo: Receber uma pergunta sobre a disponibilidade de um medicamento específico e retornar uma resposta gerada pelo ChatGPT com base nas previsões e dados atuais.

    ---

    ### Flask:

    #### Interface Web: 
    Utilizado para criar uma API web que permite a interação com o modelo de previsão e o ChatGPT.
    Exemplo: Criar endpoints para previsões de estoque e consultas ao ChatGPT, possibilitando a integração com outras partes do sistema.

- Descrever o Uso de Machine Learning / IA no Desenvolvimento:

    ### Machine Learning / Deep Learning:

    #### Modelos LSTM: 
    Utilizados para prever a demanda futura de medicamentos com base em padrões históricos de movimentação de estoque. LSTM é uma variante das Redes Neurais Recorrentes (RNNs) que lida bem com dependências de longo prazo, sendo ideal para séries temporais.
    #### Pipeline de Treinamento: 
    Inclui coleta e pré-processamento de dados, construção do modelo, treinamento e validação, e ajuste de hiperparâmetros para melhorar a precisão das previsões.
    
    ---

    ### Inteligência Artificial:

    #### ChatGPT: 
    Utilizado para fornecer respostas e recomendações em linguagem natural. A API do ChatGPT é integrada ao sistema para facilitar a consulta e fornecer insights contextuais, ajudando na tomada de decisão.

## Apresentação da Versão Beta
