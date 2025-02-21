import sys
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from typing import Optional
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Caricare le API Keys dall'ambiente
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class WebSearcher:
    """Agente che esegue ricerche su Tavily e genera un sommario con OpenAI.
    
    Questo agente combina la potenza di ricerca di Tavily con la capacità di sintesi
    di OpenAI per fornire sommari informativi su qualsiasi topic.
    """

    def __init__(self, model_name: str = "gpt-4", max_results: int = 5):
        """Inizializza il WebSearcher con parametri configurabili.
        
        Args:
            model_name: Il modello OpenAI da utilizzare (default: "gpt-4")
            max_results: Numero massimo di risultati da processare (default: 5)
        """
        self.openai = ChatOpenAI(model=model_name, openai_api_key=OPENAI_API_KEY)
        self.max_results = max_results

    def _create_summary_prompt(self, content: str) -> str:
        """Crea un prompt strutturato per la generazione del sommario.
        
        Args:
            content: Il contenuto da riassumere
            
        Returns:
            str: Il prompt strutturato
        """
        return f"""Analizza le seguenti informazioni e crea un sommario conciso e informativo:

Informazioni:
{content}

Il sommario dovrebbe:
- Essere chiaro e conciso
- Evidenziare i punti chiave
- Mantenere un tono professionale
"""

    def search(self, query):
        url = "https://api.tavily.com/search"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TAVILY_API_KEY}"  # Use the API Key from environment
        }
        data = {"query": query}

        response = requests.post(url, headers=headers, json=data)  # Changed to POST

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Errore: {response.status_code} - {response.text}")
            return None

if __name__ == "__main__":
    searcher = WebSearcher()
    result = searcher.search("Il futuro dell'intelligenza artificiale")
    print(result) 