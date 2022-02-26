import requests
import json

paremeters = {
    'amount': 10,
    'type': "boolean"
}


response = requests.get(
    'https://opentdb.com/api.php?amount=10&category=22&type=boolean',
    params=paremeters
)
response.raise_for_status()
data = response.json()
question_data = data['results']
