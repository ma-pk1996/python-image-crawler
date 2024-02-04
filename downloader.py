import requests
import json
import os

def download_images(url_file, output_folder):
    with open(url_file, 'r') as file:
        image_urls = json.load(file)

    os.makedirs(output_folder, exist_ok=True)

    for i, url in enumerate(image_urls):
        response = requests.get(url)
        if response.status_code == 200:
            file_name = f'image_{i}.jpg'
            file_path = os.path.join(output_folder, file_name)
            with open(file_path, 'wb') as image_file:
                image_file.write(response.content)
            print(f'Downloaded {file_name}')
        else:
            print(f'Error downloading image from URL: {url}')

# Example usage
json_file = 'filtered_urls.json'
output_folder = 'download'

download_images(json_file, output_folder)