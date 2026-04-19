import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

url = f'https://api.notion.com/v1/databases/{DATABASE_ID}'

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Notion-Version': '2022-06-28'
}

try:
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if 'properties' in data:
        print('Exact Property Names (with quotes):')
        for prop_name, prop_data in data['properties'].items():
            print(f'  "{prop_name}" ({prop_data["type"]})')
except Exception as e:
    print(f'Error: {e}')