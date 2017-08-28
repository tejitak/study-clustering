import requests
import os
import sys
import json

def download_image(url, timeout = 10):
    response = requests.get(url, allow_redirects=False, timeout=timeout)
    return response.content

def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)

# main
if __name__ == "__main__":
    # Read JSON data
    with open('./data/startmap.json') as data_file:    
        arr = json.load(data_file)
        for data in arr:
            url = data["logo_url"]
            filename = "./images_data/" + data["company_name"] + ".jpg"
            print(url)
            image = download_image(url)
            save_image(filename, image)
