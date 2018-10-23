import cx_Oracle
import os

os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
cur = connection.cursor()
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
    print(dokument['text'])
    text = dokument['text']
    text = text.split(' ')
    text.remove('')
    for m in matrix:
        if(m['name'] == dokument['name']):
            m['frequency'] = text.count(m['word'])

def themaDoc(matrix,nameDoc):
    tmpMatrix = []
    for m in matrix:
        if(m['name'] == nameDoc and m['frequency'] > 1):
            tmpMatrix.append(m)
    sortMatrix = sorted(tmpMatrix, key=lambda x: x['frequency'],reverse=True)
    size = 10
    if( len(sortMatrix) < size):
        size = len(sortMatrix)
    for i in range(0,size,1):
         print(tmpMatrix[i])
for name in names:
    themaDoc(matrix,name)

cur.execute('commit')
cur.close()
connection.close()
