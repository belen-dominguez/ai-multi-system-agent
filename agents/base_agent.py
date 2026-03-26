from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json

def responder(pregunta: str, area: str, archivo_conocimiento: str) -> str:
    with open(archivo_conocimiento, "r") as f:
        conocimiento = f.read()

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=f"""Sos un asistente especializado en {area}.
        Respondé la pregunta del usuario usando SOLO la siguiente información:

        {conocimiento}

        Si la respuesta no está en la información provista, decí que no tenés esa información.

        Respondé ÚNICAMENTE en formato JSON con esta estructura, sin texto adicional:
        {{
            "area": "{area}",
            "pregunta": "la pregunta recibida",
            "respuesta": "tu respuesta acá"
        }}"""),
        HumanMessage(content=pregunta)
    ]

    respuesta = llm.invoke(messages)
    return json.loads(respuesta.content)