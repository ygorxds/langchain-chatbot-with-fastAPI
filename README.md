# ChatBot com LangChain e FastAPI

Este repositório contém um exemplo básico de um chatbot construído usando [LangChain](https://langchain.com/) e [FastAPI](https://fastapi.tiangolo.com/). O projeto serve como uma introdução à construção de APIs que utilizam modelos de linguagem para gerar respostas automatizadas, permitindo fácil integração com outras aplicações.

## Visão Geral

O objetivo deste projeto é demonstrar como utilizar a biblioteca LangChain para integrar um modelo de linguagem (LLM) com uma API construída em FastAPI. O chatbot é capaz de receber entradas de texto do usuário e responder com base em um modelo de linguagem, configurado para agir como um assistente útil.

## Tecnologias Utilizadas

- **Python 3.10+**: Linguagem de programação principal.
- **FastAPI**: Framework web para a criação da API.
- **LangChain**: Biblioteca para facilitar o uso de modelos de linguagem.
- **Uvicorn**: Servidor ASGI usado para rodar a aplicação FastAPI.
- **OpenAI API**: Serviço de modelo de linguagem (opcional, configurado com a API Key).

## Funcionalidades

- **Recepção de Entradas do Usuário**: A API recebe uma string de texto via requisição HTTP POST.
- **Geração de Resposta**: Utiliza um modelo de linguagem para gerar uma resposta com base no texto fornecido.
- **Estrutura Modular**: Código organizado de maneira que facilite a extensão e a modificação.

## Estrutura do Projeto

```plaintext
mensage-bot/
├── main.py              # Código principal da aplicação FastAPI
├── requirements.txt     # Arquivo com as dependências do projeto
└── README.md            # Descrição e informações do projeto

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/ygorxds/langchain-chatbot-with-fastAPI
   cd langchain-chatbot-with-fastAPI

2. Crie e ative um ambiente virtual:

 ```bash
  python -m venv myenv
  source myenv/bin/activate  # No Windows: myenv\Scripts\activate

3. Instale as dependências:

```bash
   pip install -r requirements.txt

4. Configure sua chave de API do OpenAI:

Adicione a chave de API como uma variável de ambiente OPENAI_API_KEY.
Ou substitua diretamente no código main.py.

5. Execute o servidor FastAPI:

```bash
uvicorn main:app --reload

## Considerações Finais

Este projeto é um ponto de partida para desenvolvedores interessados em explorar a integração de modelos de linguagem em aplicações web. Ele pode ser facilmente expandido para incluir mais funcionalidades, como o gerenciamento de sessões de conversa, a integração com APIs externas, e muito mais.




