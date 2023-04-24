from pprint import pprint

import requests

# pprint(requests.get("http://127.0.0.1:8000/items/ss/").json())
pprint(requests.get("http://127.0.0.1:8000/items?name=Nails").json())
