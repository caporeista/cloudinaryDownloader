#!/usr/bin/env python
import cloudinary
import cloudinary.api
import cloudinary.utils
import os
import urllib.request

#cloudinary api bilgileri
cloudinary.config(
  cloud_name = "",
  api_key = "",
  api_secret = ""
)

#dodysların indirileceği klasör
folder_name = "Resimler" 
os.makedirs(folder_name, exist_ok=True)


page_size = 1 
next_cursor = None
while True:
    resources = cloudinary.api.resources(type='upload', max_results=page_size, next_cursor=next_cursor)
    for resource in resources['resources']:
        public_id = resource['public_id']
        file_format = resource['format']
        url = cloudinary.utils.cloudinary_url(public_id, format=file_format)[0]
        file_path = os.path.join(folder_name, f"{public_id}.{file_format}")
        print(f"Downloading {url} to {file_path}")
        urllib.request.urlretrieve(url, file_path)

    next_cursor = resources.get('next_cursor')
    if not next_cursor:
        break
