import os
import requests
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env nella directory corrente
load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))

# Ottieni l'API key
api_key = os.getenv('TAVILY_API_KEY')
print(f'Tavily API Key: {api_key}')

# Parametri della richiesta
url = 'https://api.tavily.com/search'
headers = {'Authorization': f'Bearer {api_key}'}
data = {
    'query': 'test',
    'search_depth': 'basic'
}

# Esegui la richiesta
print('\nTest Tavily API...', end=' ')
try:
    response = requests.post(url, headers=headers, json=data)
    print(f'[{response.status_code}]')
    if response.status_code != 200:
        print(f'Risposta: {response.text[:200]}...')
except Exception as e:
    print(f'Errore durante la richiesta: {e}') 