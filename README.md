# Content Creation Module

Un modulo Python per la creazione automatica di contenuti utilizzando un sistema multi-agente con CrewAI, LangChain, Tavily, OpenAI, Anthropic e Airtable.

## Struttura del Progetto

```
content_creation/
├── src/
│   ├── agents/         # Definizioni degli agenti CrewAI
│   ├── config/         # Configurazioni (logging, etc.)
│   ├── services/       # Servizi per interagire con API esterne
│   └── utils/          # Utility (gestione API keys, test connettività)
├── tests/              # Test unitari e di integrazione
├── logs/              # Log applicativi
├── .env               # File di configurazione con API keys
└── requirements.txt   # Dipendenze del progetto
```

## Requisiti

- Python 3.10 o superiore
- Ambiente virtuale (venv)
- API keys per:
  - Tavily
  - OpenAI
  - Anthropic
  - Airtable

## Installazione

1. Clona il repository e crea un ambiente virtuale:
```bash
git clone <repository-url>
cd content_creation
python -m venv venv
source venv/bin/activate  # Su Mac/Linux
venv\Scripts\activate     # Su Windows
```

2. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

3. Copia il file `.env.example` in `.env` e configura le tue API keys:
```bash
cp .env.example .env
```

## Test di Connettività

Per verificare la connessione con tutti i servizi esterni:

```bash
python -m src.utils.connectivity_test
```

## Logging

I log dell'applicazione vengono salvati in:
- File: `logs/app.log`
- Formato: JSON
- Livello predefinito: INFO

## Sicurezza

- Le API keys sono gestite in modo sicuro attraverso variabili d'ambiente
- I log sono configurati per non esporre informazioni sensibili
- La rotazione dei file di log previene la crescita incontrollata

## Sviluppo

1. Attiva l'ambiente virtuale:
```bash
source venv/bin/activate  # Su Mac/Linux
venv\Scripts\activate     # Su Windows
```

2. Esegui i test:
```bash
pytest
```

## Contribuire

1. Fai un fork del repository
2. Crea un branch per la tua feature (`git checkout -b feature/nome-feature`)
3. Committa i tuoi cambiamenti (`git commit -am 'Aggiungi feature'`)
4. Pusha al branch (`git push origin feature/nome-feature`)
5. Crea una Pull Request 