#!/usr/bin/env python3

import requests

# print version
# can also run in virtual env. venv\Scripts\activate
print(requests.__version__)
print(requests.__copyright__)

# get google home page
x = requests.get('https://www.google.com/')
print(x.status_code)