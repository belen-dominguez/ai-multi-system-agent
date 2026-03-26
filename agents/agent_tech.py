from agents.base_agent import responder

def responder_tech(pregunta: str) -> str:
    return responder(
        pregunta=pregunta,
        area="Tecnología",
        archivo_conocimiento="data/tecnologia.md"
    )