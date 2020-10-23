import sys, os, Quartz, base64, traceback
from Crypto.Cipher import AES
from datetime import datetime
from Crypto.Hash import SHA256


def run(items):
    if not 'CGSSessionScreenIsLocked' in Quartz.CGSessionCopyCurrentDictionary():
        print("bad time")
        exit()

    key = b'U#ED!AwS7B^SQ1f9xan5A@$^Cz97KwLF'
    key2 = b'wOBZkdL4FFP7o4XSSff!ehW0wlwGhTOO'
    shaBS64 = b'yx2QNm6kQ1rBp3p1KNbwXu+oKqJdNMtkob+BNFWw3J4='

    logFile = open('log','a')

    data = bytes(items, 'utf-8')
    data = base64.b64decode(data)
    try:
        cipher = AES.new(key, AES.MODE_CFB, b'This is an IV456')
        dataPC = cipher.decrypt(data).decode()
        k, time = dataPC.split(';')
        k = base64.b64decode(bytes(k,'utf-8'))
        utcUTS = datetime.utcnow().timestamp()
        if (utcUTS - float(time)) > 3:
            print(time)
            exit()
        logFile.write(str(datetime.utcnow()) + '\n')
        # final vaildate, then decode pass
        if SHA256.new(data=k).digest() != base64.b64decode(shaBS64):
            logFile.write('SHA256 vaildation fail' + '\n')
            exit()
        cipher = AES.new(key2, AES.MODE_CFB, b'This is an IV456')
        k = cipher.decrypt(k).decode()
        k = k.split()[0]

    except :
        print(traceback.print_exc())
        os.system("""osascript -e 'display dialog "Security alert"' """)

    os.system("""
    osascript -e '''
    do shell script "caffeinate -u -t 3"
    tell application "ScreenSaverEngine"
        quit
    end tell
    delay 0.2
    tell application "System Events"
        keystroke "{}"
        delay 0.5
        keystroke return
    end tell'''""".format(k))

    k = ''