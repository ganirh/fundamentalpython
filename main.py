# Fundamental Python

import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
res = requests.get(url)

print("Status Code Situs: {}".format(res.status_code))
