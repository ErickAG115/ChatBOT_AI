# Instrucciones para correr el ChatBOT
- Instalar las librerías necesarias para correr el programa
  - pip install -U langchain langchain-community langchain-ollama langchain-huggingface faiss-cpu sentence-transformers
- Instalar Ollama y correr el siguiente comando en un CMD
  - ollama run llama2:7b
- Correr el archivo build.py para crear el vectorstore
- Correr el archivo main.py para iniciar el chatbot
- Escribir una consulta (recordar que es un asistente legal y con un dataset limitado que se encuentra en la carpeta "data")
- Si desea cerrar el chat puede cerrar el programa o escribrir "salir"