import argparse
import json
from dotenv import load_dotenv
from utils.logger import get_logger
from agents.orchestrator import clasificar_pregunta
from utils.evaluator import evaluar_respuesta
from agents.agent_rrhh import responder_rrhh
from agents.agent_tech import responder_tech




logger = get_logger(__name__)
load_dotenv()

def procesar_pregunta(pregunta: str):
    logger.info(f"Pregunta recibida: {pregunta}")
    
  
    categoria = clasificar_pregunta(pregunta)
    logger.info(f"Categoría detectada: {categoria}")

    rutas = {
        "RRHH": responder_rrhh,
        "TECNOLOGIA": responder_tech,
    }


    if categoria not in rutas:
        logger.warning(f"Pregunta fuera de dominio: {pregunta}")
        return "Solo puedo responder preguntas de RRHH o Tecnología."

    respuesta = rutas[categoria](pregunta)    

    evaluacion = evaluar_respuesta(pregunta, json.dumps(respuesta, ensure_ascii=False))
    logger.info(f"Evaluación de calidad: {evaluacion['puntaje']}/10 — {evaluacion['justificacion']}")

    
    logger.info(f"Respuesta: {respuesta}")
    return respuesta

# Probamos con dos preguntas
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema multiagente de consultas")
    parser.add_argument("pregunta", type=str, help="La pregunta que querés hacer")
    args = parser.parse_args()

    respuesta = procesar_pregunta(args.pregunta)
    print(f"\n💬 {json.dumps(respuesta, ensure_ascii=False, indent=2)}")