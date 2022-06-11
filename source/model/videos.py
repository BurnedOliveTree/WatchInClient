import requests


SERVER_URI = 'localhost:8080'

def newest():
    response = requests.post(f'http://{SERVER_URI}/api/videos/newest', 
        json={'page': 1, 'size': 10})
    return response.json()['content']
