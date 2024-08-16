from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

app = FastAPI()

class ChatInput(BaseModel):
    user_input: str

# Configurando o modelo de linguagem
llm = OpenAI(temperature=0.7, openai_api_key="chave da OpenAI")

# Criando um template de prompt
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="You are a helpful assistant. {user_input}"
)

# Configurando a cadeia de processamento
chain = LLMChain(llm=llm, prompt=prompt_template)

@app.post("/chat/")
async def chat_endpoint(chat_input: ChatInput):
    response = chain.run(user_input=chat_input.user_input)
    return {"response": response}
