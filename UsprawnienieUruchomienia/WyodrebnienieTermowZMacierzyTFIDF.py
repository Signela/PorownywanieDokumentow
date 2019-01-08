import cx_Oracle
import os
import csv
from operator import itemgetter, attrgetter
# os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
# connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("SYSTEM", "Cytryna96", "localhost:1521/ORCL")
cur = connection.cursor()
cur.execute('DELETE FROM "SYSTEM"."TERM_TF_IDF"')
cur.execute('commit')
terms = []
f = open('TFIDF.csv', 'r')
with f:
    csvreader = csv.reader(f, delimiter=';')
    words = []
    headers = []
    for i in csvreader:
        for j in i:
            headers.append(j)
        break
    headers.remove(headers[0])
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        tab = []
        for j in i:
            tab.append(j)
        word = tab[0]
        tab.remove(word)
        words.append([word,tab])
    for headerNum in range(0,len(headers),1):
        term = []
        for w in words:
            term.append([w[0],w[1][headerNum]])
        matrix = sorted(term,key=lambda k: k[1], reverse=True)
        i=0
        termy = ""
        for m in matrix:
            terms.append([headers[headerNum],m[0]])
            i=i+1
            termy = termy + m[0] + ", "
            if(i==15):
                cur.execute('INSERT INTO "SYSTEM"."TERM_TF_IDF" (NAZWA_DOKUMENTU, TERM) VALUES( \'{}\', \'{}\')'.format(headers[headerNum],termy))
                cur.execute('commit')
                break;        
for m in terms:
    print(m)
myHeader = ['plik']
for i in range(1,16,1):
    myHeader.append('słowo'+' '+str(i))
f = open('TFIDF_Termy.csv', 'w', newline='')
with f:
    writer = csv.DictWriter(f, fieldnames=myHeader,delimiter=';')
    writer.writeheader()
    matrix = []
    for h in headers:
        i=0
        tab = {}
        tab.__setitem__('plik',h)
        for m in terms:
            if(h==m[0]):
                i=i+1
                tab.__setitem__('słowo'+' '+str(i),m[1])
        writer.writerow(tab)
        tab.clear()
cur.execute('commit')
cur.close()
connection.close()