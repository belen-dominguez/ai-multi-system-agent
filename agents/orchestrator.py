from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def clasificar_pregunta(pregunta: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content="""Tu única tarea es clasificar preguntas en una de estas dos categorías:
- RRHH
- TECNOLOGIA
- OTRO

Respondé ÚNICAMENTE con una de esas dos palabras, sin puntuación ni explicación."""),
        HumanMessage(content=pregunta)
    ]

    respuesta = llm.invoke(messages)
    return respuesta.content.strip()