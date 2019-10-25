import requests

r = requests.get('https://www.google.com/robots.txt')

print(r.text)