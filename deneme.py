import requests

url = 'http://localhost:8080'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    print('Response:', response.text)
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
    print(f'Detailed error: {response.text if "response" in locals() else None}')

