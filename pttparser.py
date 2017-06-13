# encoding: utf-8

import requests
from BeautifulSoup import BeautifulSoup
import json


resp = requests.get('https://www.ptt.cc/bbs/NBA/M.1497313805.A.F55.html')
soup = BeautifulSoup(resp.text)
pushes = soup.findAll('div',{'class':'push'})

data = []
for push in pushes:
    tag = push.find('span',{'class':'f1 hl push-tag'})
    tag = tag if tag else push.find('span',{'class':'hl push-tag'})
    userId = push.find('span',{'class':'f3 hl push-userid'})
    content = push.find('span',{'class':'f3 push-content'})
    time = push.find('span',{'class':'push-ipdatetime'})
    data.append({
        "tag":tag.text,
        "userId":userId.text,
        "content":content.text,
        "time":time.text
    })


with open('ptt.json', 'w') as outfile:
    json.dump(data, outfile)
