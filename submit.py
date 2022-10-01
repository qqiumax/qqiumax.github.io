import advertools as adv
import pandas as pd
import requests
import json
import time
ur = open('urlist.txt')
sitemap_urls = ur.readlines()
url = sitemap_urls
key = "387741bd4879437eb1fcc84d66b0b28e"
location = 'https://qqiumax.github.io/387741bd4879437eb1fcc84d66b0b28e.txt'
for i in url:
    i == str(i)
    endpoint = f"https://webmasters.yandex.com/indexnow?url={i}&key={key}&keyLocation={location}"
    response = requests.get(endpoint)
    print(i)
    print(endpoint)
    print(response.status_code, response.content)
          
