from agents.retriever import retriever_agent
from agents.drafter import drafter_agent
from agents.validator import validator_agent

def main():
    asking = True
    question = input("¿Cuál es tu consulta legal?: ")
    # loop to keep the chatbot going
    while asking:
        # retrieve the context of the local dataset
        retriever = retriever_agent()
        context = retriever.invoke(question)
        # draft an answer
        drafter = drafter_agent()
        answer = drafter.invoke({"context": context})
        # validate the drafter answer
        validator = validator_agent()
        validation = validator.invoke({"answer": answer})
        print("\nRespuesta legal:\n", answer)
        print("\nValidación jurídica:\n", validation)
        question = input("¿Tienes otra pregunta? Escribe 'salir' si deseas terminar el chat: ")
        # validation to end the chat
        if question.lower() == "salir":
            asking = False
if __name__ == "__main__":
    main()