import requests
from bs4 import BeautifulSoup
import json

url = 'https://unsplash.com/s/photos/knife'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
images = soup.select('img[src]')

filtered_urls = []
patterns = [
    'https://media.istockphoto.com/id/',
    'https://plus.unsplash.com/premium_photo-',
    'https://images.unsplash.com/photo-'
]

for img in images:
    src = img['src']
    for pattern in patterns:
        if src.startswith(pattern):
            filtered_urls.append(src)
            break

with open('filtered_urls.json', 'w') as file:
    json.dump(filtered_urls, file)