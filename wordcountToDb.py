# encoding: utf-8

import json
import sqlite3

delsql = "delete from word_count"
sql = "insert into word_count(article_no,word,count) values(?,?,?)"

#db = sqlite3.connect('db/2016.sqlite')
db = sqlite3.connect('db/2017.sqlite')

cur = db.cursor()

cur.execute(delsql)

#with open('files/wordcount2016.json', 'r') as f:
with open('files/wordcount2017.json', 'r') as f:
    articles = json.load(f)
    for art in articles:
        for key in art:
            for w in art[key]:
                print key + ',' + w + ',' + str(art[key][w])
                if w == ' ':
                    continue
                cur.execute(sql,(key,w,art[key][w]))

cur.close()
db.commit()
db.close()
