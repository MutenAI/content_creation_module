import os
import json
import requests
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()

# Ottieni l'API key
api_key = os.getenv('TAVILY_API_KEY')
print(f'API Key: {api_key}\n')

# Parametri della richiesta
url = 'https://api.tavily.com/search'
headers = {'Authorization': f'Bearer {api_key}'}
data = {
    'query': 'What is artificial intelligence?',
    'search_depth': 'basic',
    'include_answer': True
}

# Esegui la richiesta
print('Invio richiesta...')
response = requests.post(url, headers=headers, json=data)
print(f'Status: {response.status_code}\n')

# Mostra la risposta
if response.status_code == 200:
    result = response.json()
    print('Risposta:')
    print(json.dumps(result, indent=2))
else:
    print(f'Errore: {response.text}') 