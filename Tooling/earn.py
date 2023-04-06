#!/usr/bin/python3
import random
from typing import Text
import requests
import time 
from datetime import datetime,timezone
import socket
import struct
counter = 0
while(True):
    counter += 1
    earning = ('[ + ]  Starting payload expected earned so far: $', counter * 2 )
    print (earning)
    url= ( 'https://soclaieea.xyz/437444813342')
    host = ('soclaieea.xyz')
    headers_useragents = []
    headers_referers =[]
    headers_useragents.append('Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)')
    headers_useragents.append('Mozilla/5.0 (Linux; Android 10; SM-A102U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 Instagram 167.0.0.24.120 Android (29/10; 320dpi; 720x1402; samsung; SM-A102U; a10e; exynos7884B; en_US; 256966589)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36')
    headers_useragents.append('Mozilla/5.0 (X11; CrOS x86_64 14150.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.124 Safari/537.36')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.facebook.com/')
    headers_referers.append('http://www.instagram.com/feed/stories')
    ip =socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    header = {'Host': host,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,  
'User-Agent': random.choice(headers_useragents), 'Referrer': random.choice(headers_referers), 'Keep-Alive': str(random.randint(110,120)),'Sec-Fetch-Site' : 'none', 'Sec-Fetch-Mode': 'navigate', 
'Sec-Fetch-User' : '?1', 'Sec-Fetch-Dest' : 'document','X-Forwarded-For': ip,  'Connection' : 'close'}
    x = requests.get("https://soclaieea.xyz/437444813342", headers=header)
    if x.status_code == 200:
        timererun = random.randint(100,1800)
        now_utc = datetime.now(timezone.utc)
        logtime = now_utc.strftime("[%m/%d/%Y %H:%M UTC]]")
        print ('[ + ]', logtime, 'Script will rerun in', (timererun / 60), 'minutes')
        for text in earning:
            telebot = ('https://api.telegram.org/bot5083642153:AAFu9dkVW0aUed3F1I8yDA03X5yonjF7Qas/sendMessage?chat_id=1226111204&text="{}"'.format(text))
            requests.get(telebot)
        time.sleep(timererun)
    else:
        error = ('[ + ]  A failure has presented status code:',x.status_code)
        print ('[ + ]  A failure has presented status code:',x.status_code, 'please recheck everything is ok')
        for text in error:
            telebot = ('https://api.telegram.org/bot5083642153:AAFu9dkVW0aUed3F1I8yDA03X5yonjF7Qas/sendMessage?chat_id=1226111204&text="{}"'.format(text))
            requests.get(telebot)
        break