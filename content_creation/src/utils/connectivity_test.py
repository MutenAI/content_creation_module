import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

def test_tavily():
    print('
Test Tavily API...')
    try:
        headers = {'Authorization': f'Bearer {os.getenv("TAVILY_API_KEY")}'}
        response = requests.post('https://api.tavily.com/search',headers=headers,json={'query':'What is AI?','search_depth':'basic','include_answer':True})
        print(f'Status: {response.status_code}')
        if response.status_code == 200:
            result = response.json()
            print('[OK] Connessione riuscita')
            print('
Risposta AI:')
            print(result.get('answer','')[:200])
            print(f'
Risultati trovati: {len(result.get("results",[]))}')
        else:
            print(f'[ERRORE] {response.text}')
    except Exception as e:
        print(f'[ERRORE] {str(e)}')

def test_openai():
    print('
Test OpenAI API...')
    try:
        headers = {'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'}
        response = requests.get('https://api.openai.com/v1/models',headers=headers)
        print(f'Status: {response.status_code}')
        if response.status_code == 200:
            print('[OK] Connessione riuscita')
            models = response.json().get('data',[])
            print(f'Modelli disponibili: {len(models)}')
        else:
            print(f'[ERRORE] {response.text}')
    except Exception as e:
        print(f'[ERRORE] {str(e)}')

def test_anthropic():
    print('
Test Anthropic API...')
    try:
        headers = {'x-api-key':os.getenv('ANTHROPIC_API_KEY'),'anthropic-version':'2023-06-01','content-type':'application/json'}
        response = requests.post('https://api.anthropic.com/v1/messages',headers=headers,json={'model':'claude-3-haiku-20240307','messages':[{'role':'user','content':'Say hello'}],'max_tokens':1024})
        print(f'Status: {response.status_code}')
        if response.status_code in [200,201]:
            print('[OK] Connessione riuscita')
            result = response.json()
            if 'content' in result:
                print('
Risposta:')
                for c in result['content']:
                    if c['type']=='text': print(c['text'])
        else:
            print(f'[ERRORE] {response.text}')
    except Exception as e:
        print(f'[ERRORE] {str(e)}')

def test_airtable():
    print('
Test Airtable API...')
    try:
        base_id = os.getenv('AIRTABLE_BASE_ID')
        table = os.getenv('AIRTABLE_TABLE_NAME')
        headers = {'Authorization':f'Bearer {os.getenv("AIRTABLE_API_KEY")}'}
        response = requests.get(f'https://api.airtable.com/v0/{base_id}/{table}',headers=headers,params={'maxRecords':3})
        print(f'Status: {response.status_code}')
        if response.status_code == 200:
            print('[OK] Connessione riuscita')
            records = response.json().get('records',[])
            print(f'Records trovati: {len(records)}')
        else:
            print(f'[ERRORE] {response.text}')
    except Exception as e:
        print(f'[ERRORE] {str(e)}')

if __name__ == '__main__':
    print('
Test di Connettività alle API
========================')
    load_dotenv()
    test_tavily()
    test_openai()
    test_anthropic()
    test_airtable()
    print('
Test completati.')