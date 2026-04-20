import requests
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

def send_slack_notification(file_name: str, task: str, claude_response: str) -> bool:
    """Send notification to Slack when PDF is processed."""
    
    message = {
        'text': f'📄 PDF Processed: {file_name}',
        'blocks': [
            {
                'type': 'header',
                'text': {
                    'type': 'plain_text',
                    'text': '✅ PDF Workflow Complete'
                }
            },
            {
                'type': 'section',
                'fields': [
                    {
                        'type': 'mrkdwn',
                        'text': f'*File:*\n{file_name}'
                    },
                    {
                        'type': 'mrkdwn',
                        'text': f'*Task:*\n{task}'
                    }
                ]
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'*Claude Response:*\n```{claude_response[:500]}...```'
                }
            }
        ]
    }
    
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        return response.status_code == 200
    except Exception as e:
        print(f'Slack Error: {e}')
        return False