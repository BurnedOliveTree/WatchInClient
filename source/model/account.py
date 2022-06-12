import logging
import requests


SERVER_URI = 'localhost:8080'

def login(username: str, password: str, remember_me: bool):
    response = requests.post(f'http://{SERVER_URI}/api/account/login', 
        params={'username': username, 'password': password, 'remember-me': remember_me})
    logging.info(f'Received response from /api/account/login with code {response.status_code}')
    return response.json()
