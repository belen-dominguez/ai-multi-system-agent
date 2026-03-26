from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json

def evaluar_respuesta(pregunta: str, respuesta: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content="""Sos un evaluador de calidad de respuestas de IA.
Tu tarea es evaluar qué tan bien una respuesta contesta la pregunta original.

Respondé ÚNICAMENTE en formato JSON con esta estructura, sin texto adicional:
{
    "puntaje": <número del 1 al 10>,
    "justificacion": "<una sola oración explicando el puntaje>"
}

Criterios:
- 10: respuesta completa, precisa y directa
- 7-9: respuesta correcta pero puede mejorar
- 4-6: respuesta parcial o poco clara
- 1-3: respuesta incorrecta o irrelevante"""),
        HumanMessage(content=f"Pregunta: {pregunta}\nRespuesta: {respuesta}")
    ]

    resultado = llm.invoke(messages)
    return json.loads(resultado.content)