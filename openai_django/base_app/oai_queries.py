# import settings
from django.conf import settings
import os
import openai
from dotenv import load_dotenv


# OpenAI API Key
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY
else:
    raise Exception('OpenAI API Key not found')

load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key


def get_completion(prompt):
    query = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt }]
    )
    response = query.get('choices')[0]['message']['content']
    return response
