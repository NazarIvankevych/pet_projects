import requests
import json

paremeters = {
    'amount': 10,
    'type': "boolean"
}


class CollectData:

    def __init__(self):
        self.response = ""

    def sendRequest(self):
        self.response = requests.get(
            'https://opentdb.com/api.php?amount=10&category=22&type=boolean',
            params=paremeters
        )

    def responseReceived(self):
        self.response.raise_for_status()
        data = self.response.json()
        question_data = data['results']
        return question_data


answers = CollectData()
answers.sendRequest()
print(answers.responseReceived())
