import os
from dotenv import load_dotenv

load_dotenv()

print('Test API Keys:')
keys = {'TAVILY': os.getenv('TAVILY_API_KEY'),'OPENAI': os.getenv('OPENAI_API_KEY'),'ANTHROPIC': os.getenv('ANTHROPIC_API_KEY'),'AIRTABLE': os.getenv('AIRTABLE_API_KEY')}
for k, v in keys.items():
    print(f'{k}: {"[OK]" if v else "[MANCANTE]"}')