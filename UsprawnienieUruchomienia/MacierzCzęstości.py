import cx_Oracle
import os
import csv
from math import log10
from operator import itemgetter, attrgetter
# os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
# connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("SYSTEM", "Cytryna96", "localhost:1521/ORCL")
cur = connection.cursor()
# cur.execute('DELETE FROM "C##PPAWLUK"."TEMAT_DOKUMENTU"')
cur.execute('DELETE FROM "SYSTEM"."TEMAT_DOKUMENTU"')
cur.execute('commit')
dokumentsName = cur.execute('select distinct nazwa_dokumentu from dokument')
names = []
for dokument in dokumentsName:
    names.append(dokument[0])
dokumentsText = []
j = 0
for name in names:
    dokumentsText.append({'name': name, 'text': ''})
    text = cur.execute('select tekst from dokument where nazwa_dokumentu = \'{}\''.format(name))
    for t in text:
        dokumentsText[j]['text'] = dokumentsText[j]['text'] + t[0]
    j = j + 1
allTekst = ''
for z in dokumentsText:
    allTekst = allTekst + z['text']
allTekst = allTekst.split(' ')
allTekst.remove('')
allTekst = list(set(allTekst))
matrix = []
for word in allTekst:
    for dokument in names:
        matrix.append({"name":dokument,"word": word,'frequency':0})
for dokument in dokumentsText:
    text = dokument['text']
    text = text.split(' ')
    text.remove('')
    for m in matrix:
        if(m['name'] == dokument['name']):
            m['frequency'] = text.count(m['word'])
def themaDoc(matrix,nameDoc):
    tmpMatrix = []
    sum = 0
    for m in matrix:
        if(m['name'] == nameDoc):
            sum = sum + m['frequency']
            tmpMatrix.append(m)
    sortMatrix = sorted(tmpMatrix, key=lambda x: x['frequency'],reverse=True)
    size = 15
    if( len(sortMatrix) < size):
        size = len(sortMatrix)
    tematy = ''
    for i in range(0,size,1):
        tematy = tematy + ' ' + sortMatrix[i]['word'] + ' ' + '{:.2f}%'.format((float(sortMatrix[i]['frequency'])/float(sum))*100)+','
        print("{} {:.2f}%".format(sortMatrix[i] ,(float(sortMatrix[i]['frequency'])/float(sum))*100))
#     cur.execute('INSERT INTO "C##PPAWLUK"."TEMAT_DOKUMENTU" (NAZWA_DOKUMENTU, TEMATY) VALUES( \'{}\', \'{}\')'.format(nameDoc,tematy))
    cur.execute('INSERT INTO "SYSTEM"."TEMAT_DOKUMENTU" (NAZWA_DOKUMENTU, TEMATY) VALUES( \'{}\', \'{}\')'.format(nameDoc,tematy))
    return sortMatrix
tmpM = []
for name in names:
    tmpM.append(themaDoc(matrix,name))
for i in tmpM:
    print(i)
cur.execute('commit')
cur.close()
connection.close()
f = open('Macierz.csv', 'w', newline='')
with f:
    fnames = ['word'] + names
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    for m in tmpM:
        for i in m:
            matrix.append(i)
    matrix = sorted(matrix, key=lambda k: k['word'])
    tab = {}
    for m in matrix:
        tab.__setitem__(m['name'],m['frequency'])
        if(matrix.index(m)%len(names) == len(names)-1):
            tab.__setitem__('word',m['word'])
            writer.writerow(tab)
            tab.clear()
f = open('MacierzBinarna.csv', 'w', newline='')
with f:
    fnames = ['word'] + names
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    for m in tmpM:
        for i in m:
            matrix.append(i)
    matrix = sorted(matrix, key=lambda k: k['word'])
    tab = {}
    for m in matrix:
        if(m['frequency']>0):
            tab.__setitem__(m['name'],1)
        else: 
            tab.__setitem__(m['name'],0)
        if(matrix.index(m)%len(names) == len(names)-1):
            tab.__setitem__('word',m['word'])
            writer.writerow(tab)
            tab.clear()
f = open('TFIDF.csv', 'w', newline='')
with f:
    fnames = ['word'] + names
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    for m in tmpM:
        for i in m:
            matrix.append(i)
    matrix = sorted(matrix, key=lambda k: k['word'])
    tab = {}
    liczbaDokumentowWystapieniaSlowa = 0
    liczbaDokumentow = len(names)
    for m in matrix:
        if(m['frequency']>0):
            tab.__setitem__(m['name'],m['frequency'])
            liczbaDokumentowWystapieniaSlowa = liczbaDokumentowWystapieniaSlowa + 1
        else:
            tab.__setitem__(m['name'],0)
        if(matrix.index(m)%len(names) == len(names)-1):
            IDF = log10(float(liczbaDokumentow)/float(liczbaDokumentowWystapieniaSlowa))
            for name in names:
                tab.__setitem__(name,float(tab.get(name))*IDF)
            tab.__setitem__('word',m['word'])
            writer.writerow(tab)
            tab.clear()
            liczbaDokumentowWystapieniaSlowa = 0