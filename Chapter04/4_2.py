from pyquery import PyQuery as pq
import requests

response = requests.get('http://www.example.com').text  # content

print(response)

from urllib.request import urlopen

response = urlopen('http://www.example.com').read()
docTree = pq(response)
