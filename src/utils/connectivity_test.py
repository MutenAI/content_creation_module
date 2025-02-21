import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

def print_header(title):
    """Stampa un header formattato."""
    print(f"\n{title}")
    print("=" * len(title))

def format_date(date_str):
    """Converte la data ISO in formato leggibile."""
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    return dt.strftime('%d/%m/%Y %H:%M:%S')

def test_api_connection(name, test_func):
    """Test an API connection and print the result"""
    print(f"\nTesting {name} connection...")
    try:
        status_code = test_func()
        success = 200 <= status_code < 300
        print(f"✓ {name}: Success (Status {status_code})" if success else f"✗ {name}: Failed (Status {status_code})")
        return success
    except Exception as e:
        print(f"✗ {name}: Error - {str(e)}")
        return False

def test_tavily():
    """Test Tavily API"""
    api_key = os.getenv("TAVILY_API_KEY")
    
    if not api_key:
        raise ValueError("Missing Tavily API key")
    
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"query": "test", "search_depth": "basic"}
    )
    return response.status_code

def test_openai():
    """Test della connessione all'API di OpenAI."""
    print_header("Test OpenAI API")
    try:
        headers = {'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'}
        response = requests.get(
            'https://api.openai.com/v1/models',
            headers=headers
        )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            models = result.get('data', [])
            print("[OK] Connessione riuscita")
            print(f"Modelli disponibili: {len(models)}")
            
            if models:
                print("\nUltimi 5 modelli:")
                print("-" * 50)
                for model in models[:5]:
                    print(f"- {model['id']}")
        else:
            print(f"[ERRORE] Status: {response.status_code}")
            print(f"Dettagli: {response.text[:200]}")
            
    except Exception as e:
        print(f"[ERRORE] {str(e)}")

def test_anthropic():
    """Test Anthropic API"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        raise ValueError("Missing Anthropic API key")
    
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-3-opus-20240229",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": "Say hello"}]
        }
    )
    return response.status_code

def test_airtable():
    """Test Airtable API"""
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")
    api_key = os.getenv("AIRTABLE_API_KEY")
    
    if not all([base_id, table_name, api_key]):
        raise ValueError("Missing Airtable environment variables")
    
    response = requests.get(
        f"https://api.airtable.com/v0/{base_id}/{table_name}",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    return response.status_code

def main():
    """Run all API tests"""
    print("Starting API connectivity tests...")
    load_dotenv()
    
    results = {
        "Airtable": test_api_connection("Airtable", test_airtable),
        "Tavily": test_api_connection("Tavily", test_tavily),
        "Anthropic": test_api_connection("Anthropic", test_anthropic)
    }
    
    print("\nSummary:")
    for api, success in results.items():
        status = "✓" if success else "✗"
        print(f"{status} {api}")
    
    all_success = all(results.values())
    print(f"\nOverall status: {'✓ All tests passed' if all_success else '✗ Some tests failed'}")
    return all_success

if __name__ == "__main__":
    main() 