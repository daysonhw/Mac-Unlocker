import requests, base64
from Crypto.Cipher import AES

data = b'UnlosdfsfsdfjlkfgDSFNdsf'
key = b'U#ED!AwS7B!eFP7o4XSSff0hW^SQ1xan'

cipher = AES.new(key, AES.MODE_CFB, b'This is an IV456')
data = cipher.encrypt(data)
data = base64.b64encode(data).decode()
try:
    r = requests.post('http://host', data=data)
    if r.status_code != 200:
        exit()
except :
    print('Error')