import requests # pip install requests
import json
import urllib.request
from aiogram import types

from config import BALABOLA_URL

def get_congratulation(name: types.Message) -> types.Message:
  headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://yandex.ru',
    'Referer': 'https://yandex.ru/',
  }

  payload = {"query": name, "intro": 20, "filter": 1}
  params = json.dumps(payload).encode('utf8')
  req = urllib.request.Request(BALABOLA_URL, data=params, headers=headers)
  response = urllib.request.urlopen(req)

  r = json.loads(response.read().decode('utf8'))

  return f"{r['text']}"