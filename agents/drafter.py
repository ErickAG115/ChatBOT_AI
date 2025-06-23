from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# answer drafter agent
def drafter_agent():
    llm = Ollama(model="mistral")
    prompt = PromptTemplate.from_template("Redacta una respuesta legal clara y formal sobre:\n{context}")
    return LLMChain(prompt=prompt, llm=llm)