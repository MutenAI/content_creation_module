import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime

def format_date(date_str):
    """Converte la data ISO in formato leggibile."""
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    return dt.strftime('%d/%m/%Y %H:%M:%S')

# Carica le variabili d'ambiente
load_dotenv()

# Configurazione
base_id = os.getenv('AIRTABLE_BASE_ID')
table_name = os.getenv('AIRTABLE_TABLE_NAME')
api_key = os.getenv('AIRTABLE_API_KEY')

print("Configurazione Airtable:")
print("-" * 50)
print(f"Base ID: {base_id}")
print(f"Table: {table_name}")
print(f"API Key: {api_key[:8]}...{api_key[-4:]}")
print("-" * 50)

# Costruisci l'URL
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
headers = {'Authorization': f'Bearer {api_key}'}
params = {
    'maxRecords': 100,
    'view': 'Grid view',
    'sort[0][field]': 'createdTime',
    'sort[0][direction]': 'desc'
}

print("\nInvio richiesta...")
try:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])
        
        print(f"\nRecords trovati: {len(records)}")
        
        if records:
            print("\nUltimi 5 record:")
            print("-" * 50)
            
            for record in records[:5]:
                record_id = record['id']
                created_time = format_date(record['createdTime'])
                fields = record.get('fields', {})
                
                print(f"ID: {record_id}")
                print(f"Creato il: {created_time}")
                print(f"Fields: {json.dumps(fields, indent=2, ensure_ascii=False)}")
                print("-" * 50)
        else:
            print("\nNessun record trovato nella tabella")
            
    else:
        print("\nErrore nella richiesta:")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"\nErrore durante l'esecuzione: {str(e)}") 