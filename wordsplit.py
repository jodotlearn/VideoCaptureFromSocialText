# encoding: utf-8

import json
import jieba.analyse
import re
from datetime import datetime

stopWordFilePath = "dicts/stop_words.txt"

jieba.set_dictionary("dicts/dict.txt.big.txt")
jieba.analyse.set_stop_words(stopWordFilePath)
jieba.load_userdict("dicts/userdict.txt");

with open(stopWordFilePath) as f:
    doc = f.read()

doc = doc.decode('utf8')
doc = re.sub('\r\n', '\n', doc)
stop_words = doc.split('\n')
'''2016
st = datetime.strptime("06/25 17:00", "%m/%d %H:%M")
dt = datetime.strptime("06/25 17:00", "%m/%d %H:%M")
'''
'''2017'''
st = datetime.strptime("06/24 17:00", "%m/%d %H:%M")
dt = datetime.strptime("06/24 17:00", "%m/%d %H:%M")

a = []
#with open('files/goldenaward2016.json', 'r') as f:
with open('files/goldenaward2017.json', 'r') as f:
    data = json.load(f)
    time = ""
    art = {}
    for r in data:
        if r["time"] != time:
            if time != "":
                dt = datetime.strptime(r["time"], "%m/%d %H:%M")
                a.append({time: art})
            time =int((dt-st).total_seconds())
            art = {}
        words = jieba.cut_for_search(r["content"])
        print '-----------'
        print r['time'] + ':' + r['content'] + '---' + str(time)
        print '-----------'
        for word in words:
            if word not in stop_words:
                #print word
                if word in art:
                    art[word] = art[word] + 1
                else:
                    art[word] = 1


#with open('files/wordcount2016.json', 'w') as outfile:
with open('files/wordcount2017.json', 'w') as outfile:
    json.dump(a, outfile)