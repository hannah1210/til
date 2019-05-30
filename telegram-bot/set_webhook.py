import requests

token ="818657551:AAHNzRo7jswR-rD4YM-9OZ_SMys1lIJf3sE"
api_url =f'https://api.telegram.org/bot{token}'
#flask_url= f'https://c788f8be.ngrok.io/{token}'
flask_url = f'https://hannah1210.pythonanywhere.com/{token}'
set_url=f'{api_url}/setWebhook?url={flask_url}'

response = requests.get(set_url)
print(response.text)