from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

message = client.messages.create(
    model='claude-haiku-4-5-20251001',  # ← Use this
    max_tokens=100,
    messages=[
        {'role': 'user', 'content': 'Say hello!'}
    ]
)

print(message.content[0].text)