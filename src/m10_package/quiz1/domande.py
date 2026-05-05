# Funzioni per gestire le domande (rappresentate come dizionari):
# - `crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:`
#   - `risposta` è l'indice 0-based dell'opzione corretta
# - `info_domanda(domanda: dict) -> str:`
#   - Restituisce una stringa leggibile con domanda + opzioni numerate
# - `risposta_valida(domanda: dict, scelta: int) -> bool:`
#   - Verifica se la scelta (1-based) è valida
# - `verifica_risposta(domanda: dict, scelta: int) -> bool:`
#   - Restituisce True se la scelta (1-based) è corretta

def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    diz = {
    "testo": testo,
    "opzioni": opzioni,
    "risposta": risposta
    }
    return diz

def info_domanda(domanda:dict) -> str:
    testo = domanda.get("testo", "domanda senza testo")
    opzioni = domanda.get("opzioni", [])
    opzioni_formattate = "\n".join(f"{i+1}. {opzione}" for i, opzione in enumerate(opzioni))
    return f"{testo}\n{opzioni_formattate}"

def risposta_valida(domanda: dict, scelta: int) -> bool:
    opzioni = domanda.get("opzioni", [])
    return 1 <= scelta <= len(opzioni)

def verifica_risposta(domanda: dict, scelta: int) -> bool:
    if not risposta_valida(domanda, scelta):
        raise ValueError("Scelta non valida")
    risposta_corretta = domanda.get("risposta", -1)
    return scelta - 1 == risposta_corretta
