import requests
from requests import Response
import json

class Request:
    def __init__(self, name) -> None:
        self.name = name
    
    def post(self, url: str, header={}, body={}) -> Response:
        with open(f'tokens/{self.name}.txt', 'r') as file:
            header = {**header, 'Authorization': file.read().strip(), 'Content-Type': 'application/json'}

        return requests.post(url, headers=header, data=json.dumps(body))
        
    