from Crypto.Cipher import AES
import requests, getpass

passwd = getpass.getpass()
# countFile = open('log', 'w+')
# count = countFile.read()
data = bytes(passwd, 'utf-8')

key = b'U#ED!AwS7B!eFP7o4XSSff0hW^SQ1xan'
cipher = AES.new(key, AES.MODE_CFB, 'This is an IV456')
encrypt = cipher.encrypt(data)
print(encrypt)
data1 = {'arg1':encrypt.decode('utf-8')}


# post = requests.post('http://host:11451', data=data1)
# if post.status_code == 200
#     countFile.write(str(int(count) + 1))