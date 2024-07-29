import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer lY7VQ8OGXvyXiTqGyIC65Qz8mD3tWjc4gSxOPL7fg7T'
P['message'] = '本機圖片'
F['imageFile'] = open('pexels-photo-747964-scaled.jpeg', 'rb')
requests.post(URL, headers=H, params=P, files=F)