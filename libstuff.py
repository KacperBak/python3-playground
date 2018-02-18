import requests


def play_request():
    r = requests.get('https://api.github.com/events')
    print(r)