import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

print(f'API Key: {NOTION_API_KEY[:20]}...')
print(f'Database ID: {DATABASE_ID}')

url = 'https://api.notion.com/v1/pages'

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

data = {
    'parent': {
        'database_id': DATABASE_ID.replace('-', '')
    },
    'properties': {
        'Title': {
            'title': [
                {
                    'text': {
                        'content': 'Test from Python'
                    }
                }
            ]
        }
    }
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f'Status: {response.status_code}')
    print(f'Response: {response.json()}')
except Exception as e:
    print(f'Error: {e}')
