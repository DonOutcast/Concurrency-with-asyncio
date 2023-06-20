import requests

def get_status(url: str) -> int:
    response = requests.get(url)
    return response.status_code

url = 'https://www.example.com'
print(get_status(url))
print(get_status(url))

