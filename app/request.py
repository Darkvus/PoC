import requests

ip = 'http://0.0.0.0:8000/' # sustituimos esta url por el contenedor docker

while True:
    req = requests.get(ip)
    print(req.text)
