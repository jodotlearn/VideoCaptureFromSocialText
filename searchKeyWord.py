# encoding: utf-8
import json
import pymysql
import re
import sqlite3
import webbrowser
import sys

def main():
    namesFilePath = "files/names.json"
    who = sys.argv[1].decode('utf8').upper()
    nm = ""
    with open(namesFilePath,'r') as f:
        names = json.load(f)
        for name in names:
            if name.find(who) >= 0:
                nm = name

        if nm == "":
            nm = who

    calSql = "SELECT SUM(COUNT),AVG(COUNT) FROM word_count WHERE word REGEXP ?"
    fetchSql = "SELECT article_no,SUM(COUNT) FROM word_count WHERE word REGEXP ? GROUP BY article_no ORDER BY article_no"

#    db = sqlite3.connect('db/2016.sqlite')
    db = sqlite3.connect('db/2017.sqlite')

    def regexp(expr, item):
        nms = expr.split("|")
        for w in nms:
            if w == item:
                return True
        return False

    db.create_function("REGEXP", 2, regexp)
    cur = db.cursor()
    cur.execute(calSql,[nm])
    calResult = cur.fetchone()
    average = calResult[1]
    print average
    cur.execute(fetchSql,[nm])
    result = cur.fetchall()
    conti_a = []
    conti_b = []
    for r in result:
        if r[1] >= average:
            if len(conti_b) > 0:
                if r[0]-conti_b[len(conti_b)-1] <= 60:
                    conti_b.append(int(r[0]))
                else:
                    if len(conti_b) >= len(conti_a):
                        del conti_a[:]
                        conti_a = conti_b
                    conti_b = []
                    conti_b.append(int(r[0]))
            else:
                conti_b.append(int(r[0]))

    cur.close()
    db.close()
    result = []
    if len(conti_b) > len(conti_a):
        result = conti_b
    else:
        result = conti_a

    print conti_a
    print conti_b
    print result
    if (len(result) > 0):
        print result
        #videourl = "https://www.youtube.com/watch?v=yBitBNHSnhE&t=" + str(result[0])
        videourl = "https://www.youtube.com/watch?v=h1mqBufsZ6M&t=" + str(result[0])
        webbrowser.open(videourl)
    else:
        print 'not found'

if __name__ == "__main__":
    main()
