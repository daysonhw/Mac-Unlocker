import time, androidhelper

ssid = 'xx:xx:xx:xx:xx'

ad = androidhelper.Android()
wifiInfo = ad.wifiGetConnectionInfo().result
if not ad.checkScreenOn().result:
    # OrientatS = 
    # AccelerS = 
    if wifiInfo['rssi'] > -80 and wifiInfo['rssi'] < -67  and wifiInfo['bssid'] == ssid:
        ad.batteryStartMonitoring()
        time.sleep(0.1)
        if ad.batteryGetStatus().result != 2:
            ad.batteryStopMonitoring()
            exit()
        ad.batteryStopMonitoring()
        # ad.batteryGetPlugType() #dumpsys battery :Wireless powered: false
    # elif 
    else: 
        print(wifiInfo)
        exit()
else:
    print('auth though screenlock')
    #todo sent notification

print('Vaildate Success')
#end of vaildation


import sys, subprocess, base64, requests
from Crypto.Cipher import AES
from datetime import datetime
if sys.argv[2] != 'unlock':
    print(sys.argv)
    print(sys.argv[2])
    exit()
f = open('unlock-log','a')
f.write(str(datetime.utcnow().timestamp()))

key = b'U#ED!g3NiZJRSfSQB!uzJ1xan'
data = b'yOls7AwS7B!DAAwS7XSQf0hW^TE='

cipher = AES.new(key, AES.MODE_CFB, b'This is an IV456')
data = data + b';' + bytes(str(datetime.utcnow().timestamp()),'utf-8')
data = cipher.encrypt(data)
data = base64.b64encode(data).decode()
data = {'arg1':data}

print(data)
# REST post
# TODO: Force SSL Option
r = requests.post('http://YourDomain',data=data)
if r.status_code != 200:
    print('Fail')
print('Success')