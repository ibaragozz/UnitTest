import requests

def get_dog():
   url = f'https://dog.ceo/api/breeds/image/random'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None
