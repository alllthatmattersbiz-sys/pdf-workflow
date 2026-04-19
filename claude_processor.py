from anthropic import Anthropic

client = Anthropic()

def process_pdf_with_claude(text: str, task: str = 'summarize') -> str:
    """Send extracted PDF text to Claude for processing."""
    
    prompts = {
        'summarize': 'Summarize this text in 3 bullet points:',
        'extract_entities': 'Extract key entities (people, dates, numbers) from this text:',
        'organize': 'Organize this content into a structured format:'
    }
    
    prompt = prompts.get(task, 'Summarize this text:')
    
    message = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=1024,
        messages=[
            {'role': 'user', 'content': f'{prompt}

{text}'}
        ]
    )
    
    return message.content[0].text
