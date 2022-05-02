<<<<<<< HEAD
import requests

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
# print(question_data)
=======
import requests

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
# print(question_data)
>>>>>>> 6bb0f90e7b2042da98278b61b14da243c44df510
