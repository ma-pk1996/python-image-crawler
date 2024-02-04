# Getting Started with Data Crawler in python

This project was bootstrapped with [requests and beautifulsoup4](https://pypi.org/project/requests).

Note : This project only works for https://unsplash.com !


# Installation

!!! this website https://unsplash.com needs VPN for exploring

Suggested VPN : https://1111-releases.cloudflareclient.com/windows/Cloudflare_WARP_Release-x64.msi

Required dependencies :

1. requests
2. beautifulsoup4

Run this command : pip install requests beautifulsoup4

# How to work with

Step 1 : Change the keyword "knife" in crawler.py line 5 url variable to your desired keyword

Step 2 : Run this command => python crawler.py
Note : the urls of all images are now stored in the filtered_urls.json file

Step 3 : Run this command => python downloader.py
Note : when the code is done all of the images are now stored in the download folder

### HAPPY SCRAPING ###