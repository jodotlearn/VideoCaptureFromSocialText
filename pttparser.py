# encoding: utf-8

import requests
import json
from BeautifulSoup import BeautifulSoup

'''2016
articles = ["https://www.ptt.cc/bbs/Golden-Award/M.1466845257.A.224.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466847045.A.77F.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466848820.A.01C.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466850642.A.3D5.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466852439.A.442.html",#頒獎典禮
               "https://www.ptt.cc/bbs/Golden-Award/M.1466854126.A.8A0.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466855979.A.B5D.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466858019.A.5F2.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466859608.A.304.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466861507.A.957.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466863404.A.995.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466865018.A.296.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466866808.A.F59.html",
               "https://www.ptt.cc/bbs/Golden-Award/M.1466868605.A.87C.html"
               ]
'''

'''2017'''
articles = [
    "https://www.ptt.cc/bbs/Golden-Award/M.1498294812.A.7EE.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498296608.A.447.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498298419.A.7E2.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498300213.A.66A.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498302008.A.4F5.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498302103.A.429.html",#show1
    "https://www.ptt.cc/bbs/Golden-Award/M.1498303065.A.FDD.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498303758.A.E39.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498303920.A.426.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498305430.A.BE8.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498305905.A.C7A.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498307436.A.8B0.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498307503.A.EBE.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498309222.A.FE3.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498309510.A.A9B.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498311017.A.DC8.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498311160.A.BA4.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498312851.A.629.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498313274.A.877.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498314600.A.625.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498313888.A.A42.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498315240.A.109.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498315112.A.548.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498316362.A.B1F.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498316144.A.E80.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498316690.A.F7A.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498317144.A.B83.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498317696.A.EE2.html",
    "https://www.ptt.cc/bbs/Golden-Award/M.1498318057.A.F41.html"
]

data = []
for article in articles:
    resp = requests.get(article)
    soup = BeautifulSoup(resp.text)
    pushes = soup.findAll('div',{'class':'push'})
    for push in pushes:
        tag = push.find('span',{'class':'f1 hl push-tag'})
        tag = tag if tag else push.find('span',{'class':'hl push-tag'})
        userId = push.find('span',{'class':'f3 hl push-userid'})
        content = push.find('span',{'class':'f3 push-content'})
        time = push.find('span',{'class':'push-ipdatetime'})
        data.append({
            "tag":tag.text,
            "userId":userId.text,
            "content":content.text.replace(": ",""),
            "time":time.text
        })


#with open('files/goldenaward2016.json', 'w') as outfile:
with open('files/goldenaward2017.json', 'w') as outfile:
    json.dump(data, outfile)
