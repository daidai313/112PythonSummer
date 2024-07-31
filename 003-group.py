import requests

IMG = 'https://i2.kknews.cc/CqoTovlCdvBUyiF0JX4bGPOG0Ih4xymAgA/0.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer RJ8ZEmHu1TDQb7CGkW2mYZlxT1qyXg6cWVmFElc87zf'
P['message'] = '群組網路圖片'
F['imageFile'] = requests.get(IMG).content
requests.post(URL, headers=H, params=P, files=F)