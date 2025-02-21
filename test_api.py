import os
import requests
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()

def main():
    # Stampa le chiavi disponibili
    print("\nVerifica chiavi API:")
    print("-------------------")
    keys = {
        "Tavily": os.getenv("TAVILY_API_KEY"),
        "OpenAI": os.getenv("OPENAI_API_KEY"),
        "Anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "Airtable": os.getenv("AIRTABLE_API_KEY")
    }
    
    for name, key in keys.items():
        status = "[OK]" if key else "[MANCANTE]"
        print(f"{name}: {status}")

    # Test Tavily
    print("\nTest Tavily API:")
    try:
        response = requests.get(
            "https://api.tavily.com/search",
            params={
                "api_key": os.getenv("TAVILY_API_KEY"),
                "query": "test"
            }
        )
        print("[OK] Connessione riuscita" if response.ok else "[ERRORE] Richiesta fallita")
    except Exception as e:
        print(f"[ERRORE] {str(e)}")

    # Test Airtable
    print("\nTest Airtable API:")
    try:
        response = requests.get(
            f"https://api.airtable.com/v0/{os.getenv('AIRTABLE_BASE_ID')}/{os.getenv('AIRTABLE_TABLE_NAME')}",
            headers={"Authorization": f"Bearer {os.getenv('AIRTABLE_API_KEY')}"}
        )
        print("[OK] Connessione riuscita" if response.ok else "[ERRORE] Richiesta fallita")
    except Exception as e:
        print(f"[ERRORE] {str(e)}")

if __name__ == "__main__":
    main() 