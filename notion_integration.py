import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

def save_to_notion(title: str, content: str, task: str, claude_response: str) -> bool:
    """Save PDF processing results to Notion."""
    
    url = 'https://api.notion.com/v1/pages'
    
    headers = {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    
    data = {
        'parent': {
            'database_id': DATABASE_ID
        },
        'properties': {
            'Title': {
                'title': [
                    {
                        'text': {
                            'content': title
                        }
                    }
                ]
            },
            'Content': {
                'rich_text': [
                    {
                        'text': {
                            'content': content[:2000]
                        }
                    }
                ]
            },
            'Task': {
                'rich_text': [
                    {
                        'text': {
                            'content': task
                        }
                    }
                ]
            }
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception as e:
        print(f'Error: {e}')
        return False