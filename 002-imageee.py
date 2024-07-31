import requests

IMG = 'https://i2.kknews.cc/CqoTovlCdvBUyiF0JX4bGPOG0Ih4xymAgA/0.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer lY7VQ8OGXvyXiTqGyIC65Qz8mD3tWjc4gSxOPL7fg7T'
P['message'] = '網路圖片'
F['imageFile'] = requests.get(IMG).content
requests.post(URL, headers=H, params=P, files=F)