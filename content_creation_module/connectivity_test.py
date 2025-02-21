import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_tavily():
    try:
        headers = {'X-API-Key': os.getenv('TAVILY_API_KEY')}
        response = requests.get('https://api.tavily.com/health', headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f'Errore Tavily: {e}')
        return False

def test_openai():
    try:
        headers = {'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'}
        response = requests.get('https://api.openai.com/v1/models', headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f'Errore OpenAI: {e}')
        return False

def test_anthropic():
    try:
        headers = {'x-api-key': os.getenv('ANTHROPIC_API_KEY')}
        response = requests.get('https://api.anthropic.com/v1/messages', headers=headers)
        return response.status_code in [200, 401]  # 401 means the key is valid but needs authentication
    except Exception as e:
        print(f'Errore Anthropic: {e}')
        return False

def test_airtable():
    try:
        base_id = os.getenv('AIRTABLE_BASE_ID')
        table_name = os.getenv('AIRTABLE_TABLE_NAME')
        headers = {'Authorization': f'Bearer {os.getenv("AIRTABLE_API_KEY")}'}
        response = requests.get(f'https://api.airtable.com/v0/{base_id}/{table_name}', headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f'Errore Airtable: {e}')
        return False

print('
Test Connettività API:
-------------------')
tests = {
    'Tavily': test_tavily,
    'OpenAI': test_openai,
    'Anthropic': test_anthropic,
    'Airtable': test_airtable
}

for api, test_func in tests.items():
    result = test_func()
    print(f'{api}: {"[OK]" if result else "[ERRORE]"}')