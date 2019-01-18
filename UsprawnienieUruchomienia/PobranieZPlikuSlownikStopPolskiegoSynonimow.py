import cx_Oracle
import os
import io
# os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
# connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("SYSTEM", "Cytryna96", "localhost:1521/ORCL")
cur = connection.cursor()
cur1 = connection.cursor()
cur2 = connection.cursor()
cur3 = connection.cursor()
cur4 = connection.cursor()
cur5 = connection.cursor()
# cur.execute('DELETE FROM "C##PPAWLUK"."DOKUMENT"')
cur.execute('DELETE FROM "SYSTEM"."DOKUMENT"')
cur.execute('commit')
nameDocuments = os.listdir("dokumenty")
def clearTxt(myfile):
    myfile = myfile.replace('\n', ' ').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('/',
                                                                                                                   '').replace(
        '\\', '').replace(';', '').replace('"', ' ').replace('\'', ' ').replace(']', '').replace('[', '').replace(')',
                                                                                                                  '').replace(
        '(',
        '').replace(
        ':', '').replace('`', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace(
        '^', '').replace('&', '').replace('*', '').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=',
                                                                                                                 ' ').replace(
        '0', '').replace('1', '').replace('—', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6',
                                                                                                              '').replace(
        '7', '').replace('8', '').replace('9', '').replace('>', ' ').replace('<', ' ').replace('{', '').replace('}',
                                                                                                                '').replace(
        '§', '').replace('\', '').replace('\\ufeff', '').replace(' ', ' ').replace('–', ' ').replace('“', '').replace(
        '„', '').replace('…', '').replace('	', '').replace('’', ' ').replace('”', '').replace('  ', ' ').replace(
        '  ', ' ')
    return myfile
def stopList(myfile):
    replaceFile = myfile
    for word in myfile:
        stopword = cur1.execute(
            'select STWORD from STOPWORDS where STWORD = \'{}\' and rownum=1'.format(
                word))
        for i in stopword:
            replaceFile.remove(i[0])
    removeTab = {'	', '\n', ''}
    for remove in removeTab:
        while (remove in replaceFile):
            replaceFile.remove(remove)
    return replaceFile
def slowikPolskiego(replaceFile):
    j = 0
    for word in replaceFile:
        dictionary = cur2.execute(
            'select slow_forma_podstawowa from slownik where slow_wyraz = \'{}\' and rownum=1'.format(
                word))
        for i in dictionary:
            print("zmieniam {} na {}".format(word,i[0]))
            replaceFile.__setitem__(j, i[0])
            j = j + 1
    return replaceFile
def slowikSynonimow1(replaceFile):
    j = 0
    for word in replaceFile:
        thesaurus = cur.execute(
            'select slow_forma_podstawowa from slownik_synonimow where slow_wyraz = \'{}\' and slow_wyraz != slow_forma_podstawowa and rownum=1 '.format(
                word))
        for i in thesaurus:
            replaceFile.__setitem__(j, i[0])
            j = j + 1
    return replaceFile
def slowikSynonimow2(replaceFile):
    j = 0
    for word in replaceFile:
        thesaurus = cur.execute(
            'select slowo_podstawowe from synonimy_orginalne where (synonim1 = \'{}\' or synonim2 = \'{}\' or synonim3 = \'{}\' or synonim4 = \'{}\' or synonim5 = \'{}\' or synonim6 = \'{}\' or synonim7 = \'{}\' or synonim8 = \'{}\' or synonim9 = \'{}\' or synonim10 = \'{}\' or synonim11 = \'{}\' or synonim12 = \'{}\' or synonim13 = \'{}\' or synonim14 = \'{}\' or synonim15 = \'{}\' or synonim16 = \'{}\' or synonim17 = \'{}\' or synonim18 = \'{}\') and NOT EXISTS(select slowo_podstawowe from synonimy_orginalne where slowo_podstawowe = \'{}\') and rownum=1 '.format(
                word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word))
        for i in thesaurus:
            replaceFile.__setitem__(j, i[0])
            j = j + 1
    return replaceFile
def slowikSynonimow3(replaceFile):
    j = 0
    for word in replaceFile:
        thesaurus = cur3.execute(
            'select COLUMN1 from SYNONIMY2 where (COLUMN2 = \'{}\' or COLUMN3 = \'{}\' or COLUMN4 = \'{}\' or COLUMN5 = \'{}\' or COLUMN6 = \'{}\' or COLUMN7 = \'{}\' or COLUMN8 = \'{}\' or COLUMN9 = \'{}\' or COLUMN10 = \'{}\' or COLUMN11 = \'{}\' or COLUMN12 = \'{}\' or COLUMN13 = \'{}\' or COLUMN14 = \'{}\' or COLUMN15 = \'{}\' or COLUMN16 = \'{}\' or COLUMN17 = \'{}\' or COLUMN18 = \'{}\' or COLUMN19 = \'{}\' or COLUMN20 = \'{}\' or COLUMN21 = \'{}\' or COLUMN22 = \'{}\' or COLUMN23 = \'{}\' or COLUMN24 = \'{}\' or COLUMN25 = \'{}\' or COLUMN26 = \'{}\' or COLUMN27 = \'{}\' or COLUMN28 = \'{}\' or COLUMN29 = \'{}\' or COLUMN30 = \'{}\' or COLUMN31 = \'{}\' or COLUMN32 = \'{}\' or COLUMN33 = \'{}\' or COLUMN34 = \'{}\' or COLUMN35 = \'{}\' or COLUMN36 = \'{}\') and NOT EXISTS(select COLUMN1 from SYNONIMY2 where COLUMN1 = \'{}\') and rownum=1 '.format(
                word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word,word))
        for i in thesaurus:
            print("zmieniam {} na {}".format(word,i[0]))
            replaceFile.__setitem__(j, i[0])
            j = j + 1
    return replaceFile
def pdfparser(data, nr):
    file = io.open(data, mode="r", encoding='utf-8-sig')
    myfile = file.read()
    myfile = myfile.lower()
    myfile = clearTxt(myfile)
    myfile = myfile.split(' ')
    replaceFile = stopList(myfile)
    replaceFile = slowikPolskiego(replaceFile)
    replaceFile = stopList(replaceFile)
    replaceFile = slowikSynonimow3(replaceFile)
    replaceFile = stopList(replaceFile)
    txt = ''
    for i in range(0, len(replaceFile), 1):
        txt = txt + ' ' + (replaceFile.__getitem__(i))
        if i % 200 == 0 and i != 0:
#             cur4.execute(
#                 'INSERT INTO "C##PPAWLUK"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
#                     nameDocuments[nr], txt))
            cur4.execute(
                'INSERT INTO "SYSTEM"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
                    nameDocuments[nr], txt))
            cur4.execute('commit')
            txt = ''
    if (txt != ''):
#         cur5.execute(
#             'INSERT INTO "C##PPAWLUK"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
#                 nameDocuments[nr], txt))
        cur5.execute(
            'INSERT INTO "SYSTEM"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
                nameDocuments[nr], txt))
        cur5.execute('commit')
for i in range(0, len(nameDocuments), 1):
    pdfparser(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dokumenty\{}').format(
        nameDocuments[i]), i)
cur.close()
cur1.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()
connection.close()