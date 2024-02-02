import requests
from bs4 import BeautifulSoup
import os

# Create a folder to store the downloaded images
if not os.path.exists('images'):
    os.makedirs('images')

# Send a GET request to the URL
response = requests.get('https://www.freepik.com/photos/knife-axe')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the image elements using the full XPath
for idx in range(1, 11):  # Download the first 10 images
    image_xpath = f"/html/body/main/div[3]/div/div[2]/section/figure[{idx}]/div/a/img"
    image = soup.find('img', xpath=image_xpath)

    if image:
        image_url = image['src']
        try:
            # Send a GET request to download the image
            image_response = requests.get(image_url)
            # Save the image to the 'images' folder
            with open(f'images/image_{idx}.jpg', 'wb') as f:
                f.write(image_response.content)
            print(f'Downloaded image {idx}')
        except Exception as e:
            print(f'Error downloading image {idx}: {e}')
    else:
        print(f'Image {idx} not found')

print('Download complete!')