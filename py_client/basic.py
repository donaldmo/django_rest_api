import requests

get_response = requests.get('https://httpbin.org/status/200')
print(get_response)