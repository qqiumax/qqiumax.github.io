import advertools as adv
import pandas as pd
import requests
import json
import time
sitemap_urls = adv.sitemap_to_df("https://qqiumax.github.io/sitemapindex.xml")
key = "387741bd4879437eb1fcc84d66b0b28e"
url = sitemap_urls["loc"].to_list()
location = 'https://qqiumax.github.io/387741bd4879437eb1fcc84d66b0b28e.txt'
for i in url:
          endpoint = f"https://bing.com/indexnow?url={i}&key={key}&keyLocation={location}"
          response = requests.get(endpoint)
          print(i)
          print(endpoint)
          print(response.status_code, response.content)
          
