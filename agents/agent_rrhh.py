from agents.base_agent import responder

def responder_rrhh(pregunta: str) -> str:
    return responder(
        pregunta=pregunta,
        area="Recursos Humanos",
        archivo_conocimiento="data/rrhh.md"
    )