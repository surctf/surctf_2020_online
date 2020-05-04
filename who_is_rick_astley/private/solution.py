import requests

host = 'surctf.ru:31337'
page = 0
youtube_url = 'https://www.youtube.com/'
redirect = True
while redirect:
    r = requests.get(f'http://{host}/{page}')
    if not r.url.startswith(youtube_url):
        break
    page += 1

print(r.text)
