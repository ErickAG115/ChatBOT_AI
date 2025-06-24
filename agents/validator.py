from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# draft validator agent
def validator_agent():
    llm = Ollama(model="mistral")
    prompt = PromptTemplate.from_template("Revisa la siguiente respuesta legal:\n{answer}\n¿Es jurídicamente coherente? Justifica.")
    return LLMChain(prompt=prompt, llm=llm)